from playwright.sync_api import Page

from computer.surface import ComputerSurface
from computer.types import Target


class PlaywrightSurface(ComputerSurface):

    def __init__(self, page: Page) -> None:
        self.page = page

    def navigate(self, url: str) -> None:
        self.page.goto(url)

    def click(self, target: Target) -> None:
        locator = self._resolve_target(target)
        locator.click()

    def type(self, target: Target, value: str) -> None:
        locator = self._resolve_target(target)
        locator.fill(value)

    def read(self, target: Target) -> str:
        locator = self._resolve_target(target)
        return locator.inner_text()

    def observe(self) -> str:
        return self.page.locator("body").inner_text()

    def screenshot(self, path: str) -> None:
        self.page.screenshot(
            path=path,
            full_page=True,
        )

    def is_visible(self, target: Target) -> bool:
         locator = self._resolve_target(target)
         return locator.is_visible()
         

         

    def _resolve_target(self, target: Target):
        if target.strategy == "label":
            return self.page.get_by_label(
                target.value
            )

        if target.strategy == "role":
            if target.role is None:
                raise ValueError(
                    "Role is required for role strategy"
                )

            return self.page.get_by_role(
                target.role,
                name=target.value,
            )

        if target.strategy == "text":
            return self.page.get_by_text(
                target.value,
                exact=False,
            )

        if target.strategy == "css":
            return self.page.locator(
                target.value
            )

        raise ValueError(
            f"Unsupported locator strategy: {target.strategy}"
        )