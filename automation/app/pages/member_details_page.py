from playwright.sync_api import Page, expect


class MemberDetailsPage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def verify_loaded(self) -> None:
        expect(
            self.page.get_by_role(
                "heading",
                name="Member Details",
            )
        ).to_be_visible()

    def get_member_id(self) -> str:
        text = self.page.get_by_text(
            "Member ID:",
            exact=False,
        ).inner_text()

        return text.replace(
            "Member ID:",
            "",
        ).strip()

    def get_name(self) -> str:
        text = self.page.get_by_text(
            "Name:",
            exact=False,
        ).inner_text()

        return text.replace(
            "Name:",
            "",
        ).strip()

    def get_status(self) -> str:
        text = self.page.get_by_text(
            "Status:",
            exact=False,
        ).inner_text()

        return text.replace(
            "Status:",
            "",
        ).strip()

    def get_email(self) -> str:
        text = self.page.get_by_text(
            "Email:",
            exact=False,
        ).inner_text()

        return text.replace(
            "Email:",
            "",
        ).strip()

    def get_savings_balance(self) -> str:
        text = self.page.get_by_text(
            "Savings Balance:",
            exact=False,
        ).inner_text()

        return text.replace(
            "Savings Balance:",
            "",
        ).strip()