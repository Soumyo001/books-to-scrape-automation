import pytest
from playwright.sync_api import Page, expect
from config import BOOKS_HOME_URL, BOOKS_HOME_TITLE


@pytest.mark.smoke
def test_homepage_opens(home_page: Page) -> None:
    expect(home_page).to_have_url(BOOKS_HOME_URL)
    expect(home_page).to_have_title(BOOKS_HOME_TITLE)
    expect(home_page.locator("body")).to_be_visible()

    headings = home_page.locator("h1, h2, h3, h4, h5, h6")
    assert headings.count() > 0, "No headings found on homepage."

    for index in range(headings.count()):
        heading = headings.nth(index)
        expect(heading).to_be_visible()
        assert heading.inner_text().strip(), f"Heading {index+1} contains empty text"

    books_section = home_page.locator("ol.row")
    expect(books_section).to_be_visible()
    book_items = books_section.locator("article.product_pod")
    assert book_items.count() > 0, "No book items found"
    expect(book_items.first).to_be_visible()