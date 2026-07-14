from playwright.sync_api import sync_playwright
from time import sleep

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    # print(p.devices.keys())
    context = browser.new_context(
        color_scheme='dark',
        record_video_dir='.',
        **p.devices['iPhone 14']
    )
    page = context.new_page()
    page.goto('http://playwright.dev')
    print(page.title())

    page.screenshot(path='tela.png', type='png')

    sleep(8)
    browser.close()

with sync_playwright() as p:
    request = p.request.new_context()
    response = request.get('https://dog.ce/api/breeds/image/random')
    print(response.status)
    print(response.text())
    print(response.json())