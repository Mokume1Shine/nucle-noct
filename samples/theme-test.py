"""
NucleNoct color theme test file for Python.
Check comments, decorators, keywords, classes, functions, methods,
type hints, strings, f-strings, regex, numbers, booleans, dict keys,
exceptions, and comprehension syntax.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
import re


class ThemeMode(str, Enum):
    VOID = "void"
    SIGNAL = "signal"
    FROST = "frost"


@dataclass(frozen=True)
class PaletteToken:
    key: str
    value: str
    active: bool = True
    tags: list[str] | None = None


HEX_COLOR = re.compile(r"^#(?:[0-9a-fA-F]{3}){1,2}$")
THEME_NAME = "NucleNoct"


def normalize_token(token: PaletteToken, mode: ThemeMode) -> PaletteToken:
    fallback = (
        "#00A6C8"
        if mode is ThemeMode.SIGNAL
        else "#E4F4F7"
        if mode is ThemeMode.FROST
        else "#002737"
    )
    tags = sorted(set(token.tags or []))
    value = token.value if HEX_COLOR.match(token.value) else fallback
    return PaletteToken(key=token.key, value=value, active=token.active, tags=tags)


def build_preview(mode: ThemeMode, tokens: list[PaletteToken]) -> list[str]:
    visible = [token for token in tokens if token.active]
    preview: list[str] = []

    for index, token in enumerate(visible[:5]):
        normalized = normalize_token(token, mode)
        suffix = "!" if index % 3 == 2 else "."
        preview.append(f"{THEME_NAME}:{mode.value}:{index:02d} {normalized.key} => {normalized.value}{suffix}")

    return preview


def main() -> None:
    preview_tokens = [
        PaletteToken("editor.background", "#002737", tags=["base", "editor"]),
        PaletteToken("terminal.ansiMagenta", "#B46CBF", tags=["terminal", "ansi"]),
        PaletteToken("terminal.ansiBrightMagenta", "#D59AE0", tags=["terminal", "ansi"]),
        PaletteToken("chat.requestCodeBorder", "#00A6C8", tags=["chat", "accent"]),
        PaletteToken("textPreformat.foreground", "#FEB656", tags=["text", "warm"]),
        PaletteToken("invalid.example", "not-a-color", active=False, tags=["invalid"]),
    ]

    nested = {
        "palette": {
            "base": "#002737",
            "panel": "#0C3444",
            "border": "#355C68",
            "key": "#00A6C8",
            "string": "#E4F4F7",
        },
        "notes": [
            "Headings should stand out.",
            "JSON keys should be brighter than string values.",
            "Magenta should look magenta in the terminal.",
        ],
        "flags": [True, False, None],
    }

    for line in build_preview(ThemeMode.SIGNAL, preview_tokens):
        print(line)

    print(nested["palette"]["base"], " / ".join(nested["notes"]))

    sample_count = sum(index for index in range(6) if index % 2 == 0)
    print(f"{THEME_NAME=} {sample_count=}")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"preview failed: {exc!r}")
