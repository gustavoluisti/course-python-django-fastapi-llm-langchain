from playwright.sync_api import sync_playwright
from time import sleep

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    page = browser.new_page()
    page.goto('http://www.python.org/')

    news_button = page.locator('#news')
    news_button.click()

    news_list = page.query_selector_all('xpath=//*[@class="event-title"]')

    for news in news_list:
        news_title = news.text_content()
        news_link = news.query_selector('a').get_attribute('href')
        print(f'{news_title} - {news_link}' )

    browser.close()