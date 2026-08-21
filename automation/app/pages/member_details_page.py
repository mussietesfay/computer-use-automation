from computer.surface import ComputerSurface
from computer.types import Target


class MemberDetailsPage:

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
                value="Member Details",
            )
        )

    def get_member_id(self) -> str:
        text = self.surface.read(
            Target(
                strategy="text",
                value="Member ID:",
            )
        )

        return text.replace(
            "Member ID:",
            "",
        ).strip()

    def get_name(self) -> str:
        text = self.surface.read(
            Target(
                strategy="text",
                value="Name:",
            )
        )

        return text.replace(
            "Name:",
            "",
        ).strip()

    def get_status(self) -> str:
        text = self.surface.read(
            Target(
                strategy="text",
                value="Status:",
            )
        )

        return text.replace(
            "Status:",
            "",
        ).strip()

    def get_email(self) -> str:
        text = self.surface.read(
            Target(
                strategy="text",
                value="Email:",
            )
        )

        return text.replace(
            "Email:",
            "",
        ).strip()

    def get_savings_balance(self) -> str:
        text = self.surface.read(
            Target(
                strategy="text",
                value="Savings Balance:",
            )
        )

        return text.replace(
            "Savings Balance:",
            "",
        ).strip()