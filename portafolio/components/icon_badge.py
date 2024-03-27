import reflex as rx

from portafolio.styles.styles import EmSize


def icon_badge(icon: str) -> rx.Component:
    return rx.badge(
        rx.box(class_name=icon, font_size="32px") if "devicon" in icon else rx.icon(icon, size=32),
        aspect_ratio="1",
        variant="soft"
    )
