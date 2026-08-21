from computer.surface import ComputerSurface
from computer.types import Target


class LoginPage:

    def __init__(
        self,
        surface: ComputerSurface,
    ) -> None:
        self.surface = surface

    def open(self) -> None:
        self.surface.navigate(
            "http://localhost:5174"
        )

    def login(
        self,
        username: str,
        password: str,
    ) -> None:

        self.surface.type(
            Target(
                strategy="label",
                value="Username",
            ),
            username,
        )

        self.surface.type(
            Target(
                strategy="label",
                value="Password",
            ),
            password,
        )

        self.surface.click(
            Target(
                strategy="role",
                role="button",
                value="Login",
            )
        )