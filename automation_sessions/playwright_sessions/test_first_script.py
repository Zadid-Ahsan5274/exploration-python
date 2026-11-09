# sync api
''' from playwright.sync_api import Page, expect

def test_verify_page_url(page:Page):
    page.goto("https://www.automationexercise.com/") # passing URL
    my_url = page.url # getting current URL
    print("Current URL is: ", my_url) # printing current URL
    expect(page).to_have_url("https://www.automationexercise.com/") # expected URL
    
def test_verify_page_title(page:Page):
    page.goto("https://www.automationexercise.com/") # passing URL
    my_title = page.title # getting current title
    print("Current title is: ", my_title) # printing current title
    expect(page).to_have_title("Automation Exercise") # expected title '''
    
# async api
# install: pytest-asyncio
# command: pip install pytest-asyncio
from playwright.async_api import async_playwright, expect
import pytest

@pytest.mark.asyncio
async def test_verify_page_url():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        my_page = await browser.new_page()

        await my_page.goto("https://www.automationexercise.com/")

        print("Current URL is:", my_page.url)
        await expect(my_page).to_have_url("https://www.automationexercise.com/")

        await browser.close()
        
    

