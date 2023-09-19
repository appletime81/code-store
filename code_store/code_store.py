"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config

import reflex as rx

docs_url = "https://reflex.dev/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""

    pass


def navbar():
    return rx.box(
        rx.hstack(
            rx.image(src="favicon.ico"),
            rx.heading("My App"),
        ),
        rx.spacer(),
        rx.menu(
            rx.menu_button("Menu"),
        ),
        position="fixed",
        width="100%",
        top="0px",
        z_index="5",
    )


def index() -> rx.Component:
    return rx.box(
        navbar(),
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.compile()
