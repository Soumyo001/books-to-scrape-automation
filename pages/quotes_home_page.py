from playwright.sync_api import Page

class QuotesHomePage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.login_link = page.get_by_role("link", name="Login", exact=True)
        self.logout_link = page.get_by_role("link", name="Logout", exact=True)

    def open_login(self) -> None:
        self.login_link.click()