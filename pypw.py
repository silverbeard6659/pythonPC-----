import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com/")
    page.get_by_label("Search", exact=True).click()
    page.get_by_label("Search", exact=True).fill("trump debate fail")
    page.goto("https://www.google.com/search?q=trump+debate+fail&sca_esv=86a7437669578f61&source=hp&ei=YD0-Z8_MG8u3i-gP6JGKkQU&iflsig=AL9hbdgAAAAAZz5LcIx8xqWgmmiXlQfbTRM4F_tjZfuu&ved=0ahUKEwjP_KOg1-uJAxXL2wIHHeiIIlIQ4dUDCA0&uact=5&oq=trump+debate+fail&gs_lp=Egdnd3Mtd2l6IhF0cnVtcCBkZWJhdGUgZmFpbEjRY1DaMViPYXABeACQAQCYAZwBoAHSEaoBBDAuMTe4AQPIAQD4AQGYAhCgAtcQqAIKwgIKEAAYAxjqAhiPAcICChAuGAMY6gIYjwHCAg0QLhgDGNQCGOoCGI8BwgILEAAYgAQYsQMYgwHCAhEQLhiABBixAxjRAxiDARjHAcICCxAuGIAEGLEDGIMBwgIOEC4YgAQYsQMY0QMYxwHCAgUQABiABMICDhAAGIAEGLEDGIMBGIoFwgIIEC4YgAQYsQPCAgQQABgDwgIREAAYgAQYsQMYgwEYxwMYigXCAggQABiABBixA8ICCxAAGIAEGLEDGMcDwgIHEAAYgAQYCsICCBAAGIAEGMcDwgIKEAAYgAQYxwMYCpgDCJIHBDEuMTWgB8xt&sclient=gws-wiz")
    page.get_by_role("link", name="Videos").click()
    page.get_by_role("link", name="Images").click()
    page.get_by_role("button", name="Fact-checking Kamala Harris").nth(1).click()
    
        
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
