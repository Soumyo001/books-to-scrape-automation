import pytest
from urllib.parse import urlsplit
from playwright.sync_api import Page, expect
from config import QUOTES_HOME_URL
from pages.quotes_home_page import QuotesHomePage
from pages.quotes_login_page import QuotesLoginPage

@pytest.mark.regression
def test_successful_login_displays_logout_link(page: Page) -> None:
    page.goto(QUOTES_HOME_URL)

    homepage = QuotesHomePage(page)

    expect(page).to_have_title("Quotes to Scrape")
    expect(homepage.login_link).to_be_visible()
    expect(homepage.login_link).to_have_attribute("href", "/login")

    homepage.open_login()

    login_url = f"{QUOTES_HOME_URL.rstrip('/')}/login"
    expect(page).to_have_url(login_url)

    login_page = QuotesLoginPage(page)

    expect(login_page.username_input).to_be_visible()
    expect(login_page.password_input).to_be_visible()
    expect(login_page.submit_button).to_be_visible()

    with page.expect_response(
        lambda response: response.request.method == "POST" and urlsplit(response.url).path == "/login"
    ) as response_info:
        login_page.submit_credentials(
            username="automation_test",
            password="test1234"
        )

    login_response = response_info.value

    assert 200 <= login_response.status < 400, f"Login POST returned HTTP {login_response.status}"
    expect(page).to_have_url(QUOTES_HOME_URL)

    authenticated_homepage = QuotesHomePage(page)

    expect(authenticated_homepage.logout_link).to_be_visible()
    expect(authenticated_homepage.logout_link).to_be_enabled()
    expect(authenticated_homepage.logout_link).to_have_attribute("href", "/logout")
    expect(authenticated_homepage.login_link).to_have_count(0)