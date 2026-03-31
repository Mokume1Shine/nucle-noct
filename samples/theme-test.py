"""NucleNoct preview scene.

Quiet instruments, cold glow, and a small stream of signals for syntax preview.
"""

from __future__ import annotations

from dataclasses import dataclass
import re


HEX_COLOR = re.compile(r"^#(?:[0-9a-fA-F]{3}){1,2}$")


@dataclass(slots=True)
class Signal:
    key: str
    value: str
    active: bool = True


class NightWatch:
    def __init__(self) -> None:
        self._signals: list[Signal] = []

    def add(self, key: str, value: str, active: bool = True) -> "NightWatch":
        self._signals.append(Signal(key=key, value=value, active=active))
        return self

    def render(self) -> list[str]:
        visible = [signal for signal in self._signals if signal.active]
        return [f"{index}:{signal.key}={signal.value}" for index, signal in enumerate(visible)]


def normalize(lines: list[str]) -> list[str]:
    return [line if HEX_COLOR.search(line) else f"NucleNoct:{line}" for line in lines]


def main() -> None:
    watch = (
        NightWatch()
        .add("editor.background", "#002737")
        .add("terminal.ansiMagenta", "#B46CBF")
        .add("panel.border", "#234551")
        .add("silent.current", "not-a-color", active=False)
    )

    for line in normalize(watch.render()):
        print(f"night-watch {line}")


if __name__ == "__main__":
    try:
        main()
    except Exception as error:  # pragma: no cover
        raise SystemExit(f"signal lost: {error}") from error
