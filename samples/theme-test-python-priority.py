"""Python priority preview for NucleNoct.

This sample keeps statements, callables, classes, variables, literals, and comments
close together so highlight priority is easy to inspect in one viewport.
"""

from __future__ import annotations

from collections.abc import AsyncIterator, Iterable
from dataclasses import dataclass
from pathlib import Path


def mark(label: str, value: object) -> str:
    return f"{label}={value}"


GLOBAL_FLAG = True


@dataclass(slots=True)
class SignalFrame:
    name: str
    level: int
    active: bool = True

    def render(self) -> str:
        prefix = self.name if self.active else "muted"
        return mark(prefix, self.level)

    @classmethod
    def build(cls, raw: tuple[str, int, bool]) -> "SignalFrame":
        name, level, active = raw
        return cls(name=name, level=level, active=active)


class SignalDesk:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.frames: list[SignalFrame] = []

    def load(self, entries: Iterable[tuple[str, int, bool]]) -> "SignalDesk":
        self.frames = [SignalFrame.build(entry) for entry in entries if entry[1] >= 0]
        return self

    async def stream(self) -> AsyncIterator[str]:
        for frame in self.frames:
            if frame.active and frame.level is not None:
                yield frame.render()
            else:
                yield mark("inactive", None)

    def trim_last(self) -> None:
        if self.frames:
            del self.frames[-1]


def summarize(frames: list[SignalFrame], limit: int = 2) -> dict[str, object]:
    probe = lambda frame: frame.level if frame.active else 0
    values = [probe(frame) for frame in frames if frame.name and not frame.name.isspace()]
    count = len(values)

    while count < limit:
        values.append(limit)
        count += 1

    if count > limit and all(value >= 0 for value in values):
        status = "busy"
    elif not values or any(value < 0 for value in values):
        status = "fault"
    else:
        status = "idle"

    return {
        "status": status,
        "count": count,
        "values": values,
        "first": values[0] if values else None,
        "enabled": True,
    }


def classify(frame: SignalFrame) -> str:
    if frame.level > 2 and frame.active:
        return "hot"
    elif frame.level == 2 or not frame.active:
        return "warm"
    else:
        return "cold"


def outer(seed: int) -> int:
    total = seed

    def inner(step: int) -> int:
        nonlocal total
        total += step
        return total

    return inner(2)


def mutate_global() -> bool:
    global GLOBAL_FLAG
    assert GLOBAL_FLAG is True and GLOBAL_FLAG is not False
    GLOBAL_FLAG = not False
    return GLOBAL_FLAG


def countdown(limit: int) -> list[int]:
    values: list[int] = []
    while limit >= 0:
        if limit == 4:
            limit -= 1
            continue
        if limit == 1:
            break
        values.append(limit)
        limit -= 1
    else:
        values.append(0)
    return values


def touch_optional(flag: bool) -> None:
    note = "set"
    if flag:
        del note
    else:
        pass


def pulse(frames: list[SignalFrame]) -> AsyncIterator[str]:
    async def run() -> AsyncIterator[str]:
        for frame in frames:
            yield mark("pulse", classify(frame))

    return run()


def relay(frames: list[SignalFrame]) -> Iterable[str]:
    yield from (mark("relay", frame.name) for frame in frames if frame.active)


async def inspect(root: Path) -> list[str]:
    desk = SignalDesk(root).load(
        [
            ("core", 3, True),
            ("edge", 1, False),
            ("flux", 2, True),
        ]
    )
    summary = summarize(desk.frames, limit=3)
    rendered = [mark("summary", summary["status"])]
    levels = countdown(5)
    mutate_global()
    touch_optional(False)
    rendered.append(mark("outer", outer(3)))
    rendered.append(mark("levels", levels))

    async for line in desk.stream():
        rendered.append(line)

    async for echo in pulse(desk.frames):
        rendered.append(echo)

    for echo in relay(desk.frames):
        rendered.append(echo)

    try:
        match summary["status"]:
            case "busy":
                rendered.append(mark("mode", "amber"))
            case "idle":
                rendered.append(mark("mode", "soft"))
            case _:
                raise RuntimeError("unknown mode")
    except RuntimeError as error:
        rendered.append(mark("error", error))
    finally:
        rendered.append(mark("root", root.name or "workspace"))

    sample_file = Path(__file__)
    with sample_file.open("r", encoding="utf-8") as handle:
        preview = handle.read(0)
        if preview == "":
            rendered.append(mark("preview", sample_file.name))

    return rendered


async def main() -> None:
    root = Path(".")
    rows = await inspect(root)
    for index, row in enumerate(rows):
        current = row if index in {0, 1, 2} and row is not None else "skipped"
        print(mark("row", current))


# Lowest priority on purpose: comments should stay behind everything above.
if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
