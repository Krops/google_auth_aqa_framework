import logging

from playwright.sync_api import TimeoutError

import constants
from pages.base import BasePage

log = logging.getLogger(__file__)


class GmailLoginPage(BasePage):
    path = constants.GMAIL_LOGIN_URL

    def _init_locators(self) -> None:
        self.email_field = self.page.locator("input[type='email']")
        self.next_email_button = self.page.locator("#identifierNext > div > button")
        self.password_field = self.page.locator("input[type='password']")
        self.next_password_button = self.page.locator("#passwordNext > div > button")
        self.email_field_error = self.page.locator('form[method="post"] div[aria-atomic="true"] > div')
        self.password_field_error = self.page.locator('form[method="post"] div[aria-live="polite"] span')
        self.login_button = self.page.locator('a[data-action="sign in"]')

    def is_user_authorized(self, email: str) -> bool:
        return self.page.locator('div[translate="no"]').text_content() == email

    def fill_email(self, email: str) -> str:
        self.email_field.fill(email)
        return self.email_field.text_content()

    def fill_password(self, password: str) -> str:
        self.password_field.fill(password)
        return self.password_field.text_content()

    def navigate_here(self) -> None:
        """Navigate to this page using the navigation menu at the top of the page."""
        self.load_page()
        try:
            self.login_button.click(timeout=2000)
        except TimeoutError:
            log.warning("Seems page was redirected")
            pass
