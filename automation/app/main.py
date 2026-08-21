from browser import BrowserManager

from computer.playwright_surface import PlaywrightSurface

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.member_search_page import MemberSearchPage
from pages.member_details_page import MemberDetailsPage


def main() -> None:
    browser = BrowserManager()

    page = browser.start_browser()

    surface = PlaywrightSurface(page)

    try:
        login_page = LoginPage(surface)
        dashboard_page = DashboardPage(surface)
        member_search_page = MemberSearchPage(surface)
        member_details_page = MemberDetailsPage(surface)

        # --------------------------------
        # Login
        # --------------------------------

        login_page.open()

        login_page.login(
            username="admin",
            password="password",
        )

        if not dashboard_page.verify_loaded():
            raise RuntimeError(
                "Dashboard did not load"
            )

        print("Dashboard verified")

        # --------------------------------
        # Member Search
        # --------------------------------

        dashboard_page.open_member_search()

        if not member_search_page.verify_loaded():
            raise RuntimeError(
                "Member Search did not load"
            )

        print("Member Search verified")

        # --------------------------------
        # Search member
        # --------------------------------

        member_search_page.search(
            member_id="12345"
        )

        if not member_details_page.verify_loaded():
            raise RuntimeError(
                "Member Details did not load"
            )

        print("Member Details verified")

        # --------------------------------
        # Extract output
        # --------------------------------

        member_id = member_details_page.get_member_id()
        name = member_details_page.get_name()
        status = member_details_page.get_status()
        email = member_details_page.get_email()
        balance = member_details_page.get_savings_balance()

        print()
        print("Member Details")
        print("Member ID:", member_id)
        print("Name:", name)
        print("Status:", status)
        print("Email:", email)
        print("Savings Balance:", balance)
        print("Dashboard verified")

    finally:
        browser.stop_browser()


if __name__ == "__main__":
    main()