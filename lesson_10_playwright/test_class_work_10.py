from playwright.sync_api import Page, expect


def test_dropdown(page: Page ):
    page.goto("https://www.qa-practice.com/elements/select/mult_select")
    page.get_by_label("Choose the place you want to").select_option("1")
    expect(page.get_by_label("Choose the place you want to")).to_have_value("1")
    page.get_by_label("Choose how you want to get").select_option("1")
    expect(page.get_by_label("Choose how you want to get")).to_have_value("1")
    page.get_by_label("Choose when you want to go*").select_option("2")
    expect(page.get_by_label("Choose when you want to go*")).to_have_value("2")
    page.get_by_role("button", name="Submit").click()
    expect(page.locator("#result")).to_match_aria_snapshot("- paragraph: You selected\n- paragraph: to go by car to the sea tomorrow")



