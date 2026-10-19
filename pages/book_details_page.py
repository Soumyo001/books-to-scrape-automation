from playwright.sync_api import Page

class BookDetailsPage:
    """Elements displayed on each book details page"""

    def __init__(self, page: Page) -> None:
        self.page = page
        self.heading = page.locator("h1")
        self.product_summary = page.locator(".product_main")
        self.information_table = page.locator("table.table-striped")
        self.price = self.product_summary.locator(".price_color")