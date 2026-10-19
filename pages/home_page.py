from playwright.sync_api import Page, Locator

class HomePage:
    """interactions with the homepage"""

    def __init__(self, page: Page) -> None:
        self.page = page
        self.book_links = page.locator("ol.row article.product_pod h3 a")
        self.book_cards = page.locator("ol.row article.product_pod")

    def book_link(self, index: int) -> Locator:
        return self.book_links.nth(index)

    def book_price(self, index: int) -> Locator:
        return self.book_cards.nth(index).locator(".price_color")

    def open_book(self, index: int) -> None:
        self.book_link(index).click()