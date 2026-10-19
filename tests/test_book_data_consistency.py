import pytest
from playwright.sync_api import Page, expect
from config import BOOKS_HOME_URL
from pages.home_page import HomePage
from pages.book_details_page import BookDetailsPage

@pytest.mark.regression
@pytest.mark.parametrize("book_number", range(5))
def test_book_data_consistency(
    home_page: Page,
    random_book_indices: list[int],
    book_number: int
) -> None:
    homepage = HomePage(home_page)
    selected_index = random_book_indices[book_number]

    assert homepage.book_cards.count() == homepage.book_links.count(), "Book card and book link count mismatch"

    book_link = homepage.book_link(selected_index)
    homepage_title = book_link.get_attribute("title")

    assert homepage_title and homepage_title.strip(), "Selected book has no valid title"

    homepage_price_element = homepage.book_price(selected_index)

    expect(homepage_price_element).to_be_visible()

    homepage_price = homepage_price_element.inner_text().strip()

    assert homepage_price, "Selected book has no price"

    homepage.open_book(selected_index)

    details = BookDetailsPage(home_page)

    expect(details.heading).to_be_visible()
    expect(details.product_summary).to_be_visible()
    expect(details.price).to_be_visible()

    details_title = details.heading.inner_text().strip()
    details_price = details.price.inner_text().strip()

    assert homepage_title == details_title, f"Title mismatch: homepage={homepage_title}, details={details_title}"
    assert homepage_price == details_price, f"Price mismatch for {homepage_title}: homepage={homepage_price}, details={details_price}"

    home_page.go_back()

    expect(home_page).to_have_url(BOOKS_HOME_URL)
    expect(homepage.book_links.first).to_be_visible()