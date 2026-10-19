import pytest, random
from playwright.sync_api import Page, Browser, expect
from pages.home_page import HomePage
from config import BOOKS_HOME_URL


@pytest.fixture
def home_page(page: Page) -> Page:
    page.goto(BOOKS_HOME_URL)
    return page

@pytest.fixture(scope="module")
def random_book_indices(browser: Browser) -> list[int]:
    """select 5 random books from homepage"""

    context = browser.new_context()

    try:
        page = context.new_page()
        page.goto(BOOKS_HOME_URL)

        homepage = HomePage(page)
        expect(homepage.book_links.first).to_be_visible()

        total_books = homepage.book_links.count()
        assert total_books >= 5, f"Required at least 5 books, found {total_books}"

        return random.sample(range(total_books), 5)
    finally:
        context.close()