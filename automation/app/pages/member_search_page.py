from playwright.sync_api import Page, expect


class MemberSearchPage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def verify_loaded(self) -> None:
        expect(
            self.page.get_by_role(
                "heading",
                name="Member Search",
            )
        ).to_be_visible()

    def search(self, member_id: str) -> None:
        self.page.get_by_label(
            "Member ID"
        ).fill(member_id)

        self.page.get_by_role(
            "button",
            name="Search",
        ).click()