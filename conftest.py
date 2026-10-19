import pytest
from playwright.sync_api import Page

from config import BOOKS_HOME_URL


@pytest.fixture
def home_page(page: Page) -> Page:
    page.goto(BOOKS_HOME_URL)
    return page