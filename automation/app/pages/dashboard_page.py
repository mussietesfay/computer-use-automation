from playwright.sync_api import Page, expect


class DashboardPage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def verify_loaded(self) -> None:
        expect(
            self.page.get_by_role(
                "heading",
                name="Dashboard",
            )
        ).to_be_visible()

    def open_member_search(self) -> None:
        self.page.get_by_role(
            "button",
            name="Member Search",
        ).click()