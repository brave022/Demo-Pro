from pathlib import Path
from playwright.sync_api import sync_playwright
import json
ROOT=Path(__file__).parent.resolve() if Path(__file__).parent.resolve().joinpath('index.html').exists() else Path('/mnt/data/DemoBuddy')
html=(ROOT/'index.html').read_text(encoding='utf-8')
results=[]
with sync_playwright() as p:
    launch_kwargs = {'headless': True}
    if Path('/usr/bin/chromium').exists():
        launch_kwargs['executable_path'] = '/usr/bin/chromium'
        launch_kwargs['args'] = ['--no-sandbox']
    else:
        launch_kwargs['channel'] = 'msedge'
    browser=p.chromium.launch(**launch_kwargs)
    page=browser.new_page(viewport={'width':1440,'height':1000}, device_scale_factor=1)
    errors=[]
    page.on('pageerror', lambda err: errors.append(str(err)))
    page.set_content(html, wait_until='domcontentloaded')
    results.append(('load_and_title', page.title()=='DemoBuddy — Rehearse. Refine. Shine.'))
    results.append(('setup_defaults', page.locator('#projectName').input_value()=='Campus Event Finder'))
    # initial screenshot
    page.screenshot(path=str(ROOT/'evidence-home.png'), full_page=True)
    # sample flow tests hint and demo rescue
    page.get_by_role('button', name='Try the sample project').click()
    page.wait_for_selector('#sessionPanel:not(.hidden)')
    results.append(('sample_start_judge_mode', page.locator('#audienceBadge').inner_text()=='HACKATHON JUDGE'))
    page.get_by_role('button', name='Need a hint?').click()
    results.append(('hint_action', 'HINT — NOT THE ANSWER' in page.locator('#messages').inner_text()))
    page.get_by_role('button', name='Demo Rescue').click()
    results.append(('demo_rescue_action', 'DEMO RESCUE MODE' in page.locator('#messages').inner_text()))
    answers=[
      'It helps students discover campus events and register in one place instead of searching many announcements. I built the main flow.',
      'I used a responsive React interface and separated browsing from registration. I would test whether students can complete registration without help.',
      'I would honestly explain the failure, show a recorded happy path if available, and inspect logs to find the issue.'
    ]
    for a in answers:
      page.locator('#answerInput').fill(a)
      page.get_by_role('button', name='Send answer').click()
    page.wait_for_selector('#reportArea:not(.hidden)')
    report=page.locator('#reportArea').inner_text()
    results.append(('finishes_three_questions', 'Your 60-second pitch draft' in report and 'Campus Event Finder' in report))
    results.append(('stores_three_answers', page.locator('.message.user').count()==3))
    results.append(('final_score_is_visible', bool(page.locator('.score-num').inner_text().strip())))
    page.locator('#sessionPanel').screenshot(path=str(ROOT/'evidence-report-panel.png'))
    # copy button fallback path does not crash even if clipboard is denied
    page.get_by_role('button', name='Copy my summary').click()
    # restart and test recruiter mode
    page.get_by_role('button', name='Start again').click()
    page.locator('#projectName').fill('Weather Planner')
    page.locator('#projectDesc').fill('A mobile-first app that helps students plan around weather changes and outdoor campus events.')
    page.locator('#audience').select_option('recruiter')
    page.locator('#setupForm button[type=submit]').click()
    results.append(('recruiter_mode', page.locator('#audienceBadge').inner_text()=='RECRUITER MODE'))
    results.append(('recruiter_question_is_custom', 'What did you personally build' in page.locator('#messages').inner_text()))
    # blank answer guard
    page.locator('#answerInput').fill('')
    page.get_by_role('button', name='Send answer').click()
    results.append(('empty_answer_guard', 'Write a sentence first' in page.locator('#answerStatus').inner_text()))
    # responsive check
    page.set_viewport_size({'width':390,'height':844})
    results.append(('mobile_no_horizontal_overflow', page.evaluate('document.documentElement.scrollWidth <= window.innerWidth + 2')))
    # adaptive short answer branch
    page.set_viewport_size({'width':1440,'height':1000})
    page.get_by_role('button', name='Start again').click()
    page.locator('#projectName').fill('Short Answer Case')
    page.locator('#projectDesc').fill('A simple project used to test adaptive questions.')
    page.locator('#audience').select_option('beginner')
    page.locator('#setupForm button[type=submit]').click()
    page.locator('#answerInput').fill('It helps users.')
    page.get_by_role('button', name='Send answer').click()
    results.append(('short_answer_adaptive_branch','make that more concrete' in page.locator('#messages').inner_text().lower()))
    # technical branch test separately
    page.get_by_role('button', name='Start again').click()
    page.locator('#projectName').fill('Technical Decision Case')
    page.locator('#projectDesc').fill('A project with a cloud backend and frontend app.')
    page.locator('#setupForm button[type=submit]').click()
    page.locator('#answerInput').fill('I used AWS Lambda and Amazon S3 with an API so the app can serve requests and store files.')
    page.get_by_role('button', name='Send answer').click()
    results.append(('technical_answer_adaptive_branch','technical choice' in page.locator('#messages').inner_text().lower()))
    results.append(('no_page_errors', len(errors)==0))
    if errors: print('PAGE_ERRORS:', errors)
    browser.close()
(ROOT/'test-results.json').write_text(json.dumps({'summary':f"{sum(bool(v) for _,v in results)}/{len(results)} tests passed",'tests':[{'name':n,'passed':bool(v)} for n,v in results]},indent=2))
print(json.dumps({'summary':f"{sum(bool(v) for _,v in results)}/{len(results)} tests passed",'tests':[{'name':n,'passed':bool(v)} for n,v in results]},indent=2))
if not all(v for _,v in results): raise SystemExit(1)
