from playwright.sync_api import Browser, Page, Playwright, sync_playwright


class BrowserManager:
    def __init__(self) -> None:
        self.playwright: Playwright | None = None
        self.browser: Browser | None = None
        self.page: Page | None = None

    def start_browser(self) -> Page:
        self.playwright = sync_playwright().start()

        self.browser = self.playwright.chromium.launch(
            headless=False
        )

        self.page = self.browser.new_page()

        return self.page

    def stop_browser(self) -> None:
        if self.browser:
            self.browser.close()

        if self.playwright:
            self.playwright.stop()