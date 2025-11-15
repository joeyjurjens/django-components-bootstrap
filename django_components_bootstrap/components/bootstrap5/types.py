from typing import Literal

Breakpoint = Literal["sm", "md", "lg", "xl", "xxl"]
BreakpointOrAuto = int | Literal["auto"]

Size = Literal["sm", "lg"]
SizeWithXl = Literal["sm", "lg", "xl"]

Variant = Literal[
    "primary",
    "secondary",
    "success",
    "danger",
    "warning",
    "info",
    "light",
    "dark",
]

VariantWithLink = Literal[
    "primary",
    "secondary",
    "success",
    "danger",
    "warning",
    "info",
    "light",
    "dark",
    "link",
]

TextColor = Literal[
    "primary",
    "secondary",
    "success",
    "danger",
    "warning",
    "info",
    "light",
    "dark",
    "body",
    "muted",
    "white",
    "black-50",
    "white-50",
]

BgColor = Literal[
    "primary",
    "secondary",
    "success",
    "danger",
    "warning",
    "info",
    "light",
    "dark",
    "body",
    "white",
    "transparent",
]

Alignment = Literal["start", "center", "end"]
Direction = Literal["start", "end", "top", "bottom"]
Placement = Literal["start", "end", "top", "bottom"]

HeadingLevel = Literal["h1", "h2", "h3", "h4", "h5", "h6"]
ButtonTag = Literal["button", "a"]
AnchorOrButton = Literal["a", "button"]
AnchorOrSpan = Literal["a", "span"]

ButtonType = Literal["button", "submit", "reset"]
FormCheckType = Literal["checkbox", "radio", "switch"]

NavbarPlacement = Literal["fixed-top", "fixed-bottom", "sticky-top", "sticky-bottom"]
OffcanvasPlacement = Literal["start", "end", "top", "bottom"]

ThemeVariant = Literal["dark", "light"]
NavVariant = Literal["tabs", "pills", "underline"]
CardImgVariant = Literal["top", "bottom"]
SpinnerVariant = Literal["border", "grow"]

DropdownDirection = Literal["down", "up", "end", "start"]
AutoClose = Literal["true", "inside", "outside", "false"]

ContainerFluid = Breakpoint | Literal["fluid"] | bool
ResponsiveBreakpoint = Breakpoint | bool
