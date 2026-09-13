"""Server-rendered guidance for first-time learners; no JavaScript required."""
from html import escape
import json

STYLE = """
table{border-collapse:collapse;width:100%;font-size:16px}th,td{padding:12px;text-align:left;vertical-align:top;border-bottom:1px solid #d5e1dd}th{background:#e7efeb}.table-wrap{overflow:auto}code{overflow-wrap:anywhere}:root{color-scheme:light}*{box-sizing:border-box}body{margin:0;background:#f3f6f5;color:#203b39;font:18px/1.65 system-ui,sans-serif}header{border-bottom:1px solid #d5e1dd;background:white;padding:18px max(24px,calc((100% - 920px)/2))}header a{color:#234c46;text-decoration:none;font-weight:750}main{max-width:820px;margin:40px auto;padding:0 24px 60px}h1{font-size:clamp(30px,5vw,46px);line-height:1.15;letter-spacing:-1px;margin:12px 0 22px}h2{font-size:23px;line-height:1.3}p{margin:12px 0 20px}.eyebrow{font-size:13px;font-weight:750;letter-spacing:1.3px;text-transform:uppercase;color:#526d65}.card{background:white;border:1px solid #d5e1dd;border-radius:16px;padding:26px;margin:24px 0}.result{border-left:5px solid #317562}.hold{border-left-color:#ab6923}.badge{font-size:13px;font-weight:750;letter-spacing:1px;color:#326b57}.hold .badge{color:#925411}.button,button{display:inline-block;background:#245c50;color:white;border:0;border-radius:8px;padding:12px 20px;font:inherit;font-weight:650;text-decoration:none;cursor:pointer}a{color:#205d50;text-underline-offset:4px}.secondary{background:transparent;color:#245c50;border:1px solid #829e92}nav{display:flex;gap:16px;align-items:center;flex-wrap:wrap;margin:24px 0}small,.muted{color:#566c65}details{margin-top:28px;border-top:1px solid #d5e1dd;padding-top:16px}summary{cursor:pointer;font-size:16px}pre{background:#edf2f0;padding:16px;border-radius:8px;overflow:auto;font-size:15px;line-height:1.6}label{display:block;padding:14px 0;border-bottom:1px solid #e1e9e5}input{width:22px;height:22px;vertical-align:middle;margin-right:12px;accent-color:#245c50}label span{display:block;margin-left:38px;font-size:16px;color:#566c65}li{margin-bottom:10px}:focus-visible{outline:3px solid #a35c15;outline-offset:4px}.progress{font-size:15px;color:#526d65}footer{font-size:14px;border-top:1px solid #d5e1dd;padding-top:20px;margin-top:36px}@media(max-width:540px){main{margin-top:24px}.card{padding:20px}nav .button{width:100%;text-align:center}}
"""


def page(title, body):
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{escape(title)} | Vibe Deploy Guardrails</title><style>{STYLE}</style></head>'
            f'<body><header><a href="/">Vibe Deploy Guardrails</a></header><main>{body}'
            '<footer>Local practice only. These examples do not authorize a real release. '
            'Your progress is not saved; you can repeat any step.</footer></main></body></html>').encode()


def raw_result(data):
    return ('<details><summary>Optional: see what the program returned</summary>'
            '<p>This is JSON: a structured format programs use to exchange information. '
            'You do not need to memorize it. <code>true</code> means yes; '
            '<code>false</code> means no.</p><pre>' + escape(json.dumps(data, indent=2)) + '</pre></details>')


def navigation(step):
    previous = '/' if step == 1 else f'/learn?step={step-1}'
    forward = f'<a class="button" href="/learn?step={step+1}">Continue to step {step+1}</a>' if step < 5 else '<a class="button" href="/learn?step=4">Practice again</a>'
    return f'<nav>{forward}<a href="{previous}">Back</a><a href="/">Course home</a></nav>'


def home():
    return page('Your course', """<p class="eyebrow">An operator’s technical bridge · learn at your pace</p>
<h1>Learn to inspect data.<br>Then deploy with confidence.</h1>
<p>Welcome. You’ll help a fictional UAS company turn mission records into a small, controlled software system. Start with one lesson, not the whole toolchain.</p>
<div class="card"><span class="badge">START HERE · SQL</span><h2>Meet your operational data</h2><p>SQL is a way to ask questions of a database. Your first task is to find the tables and understand what one record represents. No database software installation is needed.</p><nav><a class="button" href="/lesson?name=lessons/sql/01-inspect.md">Start lesson 1</a><a href="/lesson?name=START_HERE.md">Setup help</a></nav></div>
<h2>How to use this course</h2><ol><li><strong>Read here.</strong> Course links open explanations and exercises.</li><li><strong>Practice in the terminal.</strong> Command boxes tell you where they belong. Leave the server terminal running and use a second terminal for exercises.</li><li><strong>Check your result.</strong> Each lesson gives an expected result and an unaided checkpoint. Save your own notes in the evidence folder.</li></ol>
<p>The full route takes about 12 weeks at 8–10 hours a week. You can slow down or repeat lessons. The reference solutions are examples to compare after trying.</p>
<nav><a class="button secondary" href="/course">See the course map</a><a href="/learn?step=1">Optional: 10-minute browser orientation</a></nav>
<div class="card"><h2>Your learning route</h2><p>SQL → Python and APIs → Git and tests → reproducible environments → deployment → safe release → security review → capstone.</p><p>All data is fictional. You are practicing how to ask good technical questions and show evidence, without claiming production engineering experience.</p></div>""")


def lesson(step, config, evaluate):
    intro = f'<p class="eyebrow">Lab 00 / guided browser lesson</p><p class="progress">Step {step} of 5</p>'
    if step == 1:
        data = {"status": "ok", "environment": config.environment, "version": config.version}
        body = ('<h1>Is the app responding?</h1><div class="card result"><span class="badge">APP RESPONDING</span>'
                '<h2>Your browser reached the app.</h2><p>The app received your request and generated this page.</p>'
                f'<p>Practice environment: <strong>{escape(config.environment)}</strong><br>Version label: <strong>{escape(config.version)}</strong></p></div>'
                '<h2>What does this tell us?</h2><p>It is like checking that equipment powers on. That is useful, but it does not prove every function works.</p>'
                '<p><strong>Next:</strong> we’ll check whether a release should be held.</p>' + raw_result(data))
    elif step in (2, 3):
        checks = {"review": True, "tests": step == 3, "rollback": True}
        data = {"ready": evaluate(checks), "checks": checks, "version": config.version}
        body = ('<h1>One failed check matters.</h1>' if step == 2 else '<h1>Now the evidence is complete.</h1>')
        body += result_card(data)
        body += ('<h2>Why hold?</h2><p>Someone reviewed the change and a recovery plan exists, but the functional tests failed. We fix the problem and repeat the checks before considering release.</p><p>The app itself is working: returning a hold is the correct answer.</p>' if step == 2 else '<h2>What changed?</h2><p>Only the test result changed from failed to passed. All three required checks are now present.</p><p>This is a simulated result. In real work, a person must verify the evidence and exercise release authority.</p>')
        body += raw_result(data)
    elif step == 4:
        body = """<h1>You make the call.</h1><p>Select the evidence you have, then check the result. These are practice inputs; ticking a box does not perform a real review or test.</p>
<form class="card" action="/check" method="get"><h2>Practice release checklist</h2>
<label><input type="checkbox" name="review" value="true">The change has been reviewed<span>Someone has checked what changed and why.</span></label>
<label><input type="checkbox" name="tests" value="true">The functional tests passed<span>The required behavior was checked and worked.</span></label>
<label><input type="checkbox" name="rollback" value="true">A recovery plan is ready<span>We know how to restore a known-good version.</span></label>
<p>First try leaving all boxes empty. Then try two boxes. Finally, try all three.</p><button type="submit">Check my practice release</button></form>"""
    else:
        body = """<h1>You’ve finished the browser walkthrough.</h1><div class="card"><h2>What you should be able to explain</h2><ul><li>A responding app is not proof that every function works.</li><li>A failed or missing required check means hold.</li><li>We need review, functional checks, and a recovery plan together.</li></ul></div>
<h2>Next: start the SQL track</h2><p>The browser shows you a friendly explanation. A terminal command can check the same behavior automatically. The SQL track is your next course phase.</p><p>Open the full lesson below and follow the SQL setup instructions. A <strong>smoke check</strong> is a short functional check of a running app.</p>
<p><a class="button" href="/lesson?name=START_HERE.md">Open the setup and first-lesson guide</a></p>
<details><summary>What is a terminal, and where do commands go?</summary><p>The terminal is the panel where you typed the command to start this app. Commands go there, not in the browser address bar or in a Python notebook.</p><p>Leave the app running in its terminal. Use a second terminal for checks. It must be in the course folder, the one containing <code>README.md</code> and <code>guardrails/</code>.</p><p>If you get stuck, tell your course assistant the exact step and message. You do not need to work it out by guessing.</p></details>"""
    return page(f'Step {step}', intro + body + navigation(step))


def result_card(data):
    ready = data["ready"]
    labels = {"review": "Change reviewed", "tests": "Functional tests passed", "rollback": "Recovery plan ready"}
    items = ''.join(f'<li><strong>{"Present" if data["checks"][key] else "Missing or failed"}:</strong> {label}</li>' for key, label in labels.items())
    return (f'<section class="card result {"" if ready else "hold"}"><span class="badge">{"ALL CHECKS PRESENT" if ready else "HOLD THE RELEASE"}</span>'
            f'<h2>{"The practice checklist is complete." if ready else "Required evidence is missing or failed."}</h2><ul>{items}</ul></section>')


def check_page(data):
    return page('Your practice result', '<p class="eyebrow">Lab 00 / your practice result</p><h1>Here’s what your choices mean.</h1>' + result_card(data) +
                '<p>All three checks are required. Missing evidence is a reason to hold, even if the other checks passed.</p>' +
                '<nav><a class="button" href="/learn?step=4">Try a different combination</a><a href="/learn?step=5">Continue to the recap</a></nav>' + raw_result(data))
