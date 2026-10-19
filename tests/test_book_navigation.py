import pytest
from urllib.parse import urljoin
from playwright.sync_api import Page, expect
from config import BOOKS_HOME_URL
from pages.home_page import HomePage
from pages.book_details_page import BookDetailsPage

@pytest.mark.regression
@pytest.mark.parametrize("book_number", range(5))
def test_random_book_navigation(
    home_page: Page,
    random_book_indices: list[int],
    book_number: int
) -> None:
    homepage = HomePage(home_page)
    selected_index = random_book_indices[book_number]
    book_link = homepage.book_link(selected_index)

    expected_title = book_link.get_attribute("title")
    relative_href = book_link.get_attribute("href")

    assert expected_title and expected_title.strip(), "Selected book has no valid title"
    assert relative_href and relative_href.strip(), "Selected book has no valid href"

    expected_url = urljoin(BOOKS_HOME_URL, relative_href)
    homepage.open_book(selected_index)

    expect(home_page).to_have_url(expected_url)

    details = BookDetailsPage(home_page)

    expect(details.heading).to_be_visible()
    expect(details.heading).to_have_text(expected_title)
    expect(details.product_summary).to_be_visible()
    expect(details.information_table).to_be_visible()
    assert details.information_table.inner_text().strip(), "Book information table is empty"

    home_page.go_back()

    expect(home_page).to_have_url(BOOKS_HOME_URL)
    expect(homepage.book_links.first).to_be_visible()