import re
from playwright.sync_api import Page, expect

def __init__(self, page: Page):
    self.__page = page


def test_negative_login(page: Page) -> None:
    page.goto("https://www.google.com/search?q=saucodemo&oq=saucodemo&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCDQyMzBqMGoyqAIAsAIB&sourceid=chrome&ie=UTF-8")
    page.get_by_role("link", name="Swag Labs Swag Labs https://").click()
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("user_name")
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("Aa123456")
    page.locator("[data-test=\"password\"]").press("Enter")
    page.locator("[data-test=\"login-button\"]").click()
    expect(page.locator("#root")).to_match_aria_snapshot("- text: Swag Labs")
    expect(page.locator("[data-test=\"login-container\"]")).to_match_aria_snapshot("- textbox \"Username\": user_name\n- textbox \"Password\": Aa123456\n- 'heading \"Epic sadface: Username and password do not match any user in this service\" [level=3]':\n  - button\n- button \"Login\"\n- heading \"Accepted usernames are:\" [level=4]\n- text: standard_user locked_out_user problem_user performance_glitch_user error_user visual_user\n- heading \"Password for all users:\" [level=4]\n- text: secret_sauce")
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("user_name")
    page.locator("[data-test=\"username\"]").press("Tab")
    page.locator("[data-test=\"password\"]").fill("Aa123456")
    page.locator("[data-test=\"password\"]").press("Enter")
    page.locator("[data-test=\"login-button\"]").click()
    expect(page.locator("#root")).to_match_aria_snapshot("- text: Swag Labs")
    expect(page.locator("[data-test=\"login-container\"]")).to_match_aria_snapshot("- textbox \"Username\": user_name\n- textbox \"Password\": Aa123456\n- 'heading \"Epic sadface: Username and password do not match any user in this service\" [level=3]':\n  - button\n- button \"Login\"\n- heading \"Accepted usernames are:\" [level=4]\n- text: standard_user locked_out_user problem_user performance_glitch_user error_user visual_user\n- heading \"Password for all users:\" [level=4]\n- text: secret_sauce")
    page.wait_for_timeout(2000)