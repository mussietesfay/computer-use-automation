from computer.surface import ComputerSurface
from computer.types import Target


class DashboardPage:

    def __init__(
        self,
        surface: ComputerSurface,
    ) -> None:
        self.surface = surface

    def verify_loaded(self) -> bool:
        return self.surface.is_visible(
            Target(
                strategy="role",
                role="heading",
                value="Dashboard",
            )
        )

    def open_member_search(self) -> None:
        self.surface.click(
            Target(
                strategy="role",
                role="button",
                value="Member Search",
            )
        )