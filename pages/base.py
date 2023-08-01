import abc

from playwright.sync_api import Page


class BasePage(abc.ABC):
    """Base Page."""

    base_url: str
    path: str
    page: Page
    url: str
    timeout: int = 3000

    def __init__(
            self,
            base_url: str,
            page: Page,
    ) -> None:
        """Init object instance."""
        self.base_url = base_url
        self.page = page
        self.url = self.base_url + self.path
        self._init_locators()

    def load_page(self) -> None:
        """Load page and wait till network idle."""
        self.page.goto(self.url, wait_until="domcontentloaded")
        self.wait_until_page_loaded()

    @abc.abstractmethod
    def navigate_here(self) -> None:
        """Navigate to this page using top navigation menu.

        This method is abstract and must be implemented by each page separately.
        """
        pass

    @abc.abstractmethod
    def _init_locators(self) -> None:
        pass

    def reload_page(self, timeout: int = 20000) -> None:
        """Reload page and wait till network idle."""
        self.page.reload(timeout=timeout, wait_until="networkidle")
        self.wait_until_page_loaded()

    def wait_until_page_loaded(self, timeout: int = 0) -> None:
        """Wait for loaded event on the page."""
        if timeout == 0:
            timeout = self.timeout
        self.page.wait_for_timeout(timeout)
