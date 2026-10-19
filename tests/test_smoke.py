import pytest
from playwright.sync_api import Page, expect
from config import BOOKS_HOME_URL, BOOKS_HOME_TITLE


@pytest.mark.smoke
def test_homepage_opens(home_page: Page) -> None:
    expect(home_page).to_have_url(BOOKS_HOME_URL)

    expect(home_page).to_have_title(BOOKS_HOME_TITLE)

    expect(home_page.locator("body")).to_be_visible()