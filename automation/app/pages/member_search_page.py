from computer.surface import ComputerSurface
from computer.types import Target


class MemberSearchPage:

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
                value="Member Search",
            )
        )

    def search(
        self,
        member_id: str,
    ) -> None:

        self.surface.type(
            Target(
                strategy="label",
                value="Member ID",
            ),
            member_id,
        )

        self.surface.click(
            Target(
                strategy="role",
                role="button",
                value="Search",
            )
        )