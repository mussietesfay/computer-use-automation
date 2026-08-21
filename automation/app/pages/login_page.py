from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def open(self) -> None:
        self.page.goto("http://localhost:5174")

    def login(
        self,
        username: str,
        password: str,
    ) -> None:
        self.page.get_by_label("Username").fill(username)

        self.page.get_by_label("Password").fill(password)

        self.page.get_by_role(
            "button",
            name="Login",
        ).click()