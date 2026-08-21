from browser import BrowserManager

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.member_search_page import MemberSearchPage
from pages.member_details_page import MemberDetailsPage


def main() -> None:
    browser = BrowserManager()

    page = browser.start_browser()

    try:
        login_page = LoginPage(page)
        dashboard_page = DashboardPage(page)
        member_search_page = MemberSearchPage(page)
        member_details_page = MemberDetailsPage(page)

        login_page.open()

        login_page.login(
            username="admin",
            password="password",
        )

        dashboard_page.verify_loaded()

        print("Login successful")
        print("Dashboard loaded")

        dashboard_page.open_member_search()

        member_search_page.verify_loaded()

        print("Member Search loaded")

        member_search_page.search(
            member_id="12345"
        )

        member_details_page.verify_loaded()

        print("Member Details loaded")

        member_id = member_details_page.get_member_id()
        name = member_details_page.get_name()
        status = member_details_page.get_status()
        email = member_details_page.get_email()
        balance = member_details_page.get_savings_balance()

        print("Member Details")
        print("Member ID:", member_id)
        print("Name:", name)
        print("Status:", status)
        print("Email:", email)
        print("Savings Balance:", balance)

       

        input("Press Enter to exit...")

    finally:
        browser.stop_browser()


if __name__ == "__main__":
    main()