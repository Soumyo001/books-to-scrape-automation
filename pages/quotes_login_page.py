from playwright.sync_api import Page

class QuotesLoginPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.username_input = page.locator('input[name="username"]')
        self.password_input = page.locator('input[name="password"]')
        self.submit_button = page.locator('input[type="submit"][value="Login"]')

    def submit_credentials(self, username: str, password: str) -> None:
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.submit_button.click()