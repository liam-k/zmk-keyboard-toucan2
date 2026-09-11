#!/usr/bin/env python3
from dataclasses import dataclass
from html import escape
from pathlib import Path


@dataclass(frozen=True)
class Key:
    tap: str
    hold: str = ""
    kind: str = "key"


def k(tap: str, hold: str = "", kind: str = "key") -> Key:
    return Key(tap, hold, kind)


none = k("", kind="none")

LAYERS = {
    "00-base": {
        "title": "Layer 0 — BASE",
        "note": "KOY alpha layout · hold ordinary letters for the matching Symbol action",
        "keys": [
            none, k("k", "°"), k(".", "@"), k("o", "["), k(",", "–"), k("ü", "^"),
            k("v", "!"), k("g", "<"), k("c", ">"), k("l", "="), k("z", "&"), none,
            none, k("h", "Shift"), k("a", "Ctrl"), k("e", "Alt"), k("i", "GUI"), k("y", "*"),
            k("b", "?"), k("t", "GUI"), k("r", "Alt"), k("n", "Ctrl"), k("f", "Shift"), none,
            none, k("x", "#"), k("q", "|"), k("ä", "$"), k("u", "~"), k("ö", "`"),
            k("p", "+"), k("d", "%"), k("w", "\""), k("m", "'"), k("j", ";"), none,
            k("NUM NAV", "tap: sticky · hold: momentary", "layer"), k("Space", "hold: SYM", "layer"), k("Smart Shift", "tap again: Caps Word", "modifier"),
            k("SYM", "tap: sticky · hold: momentary", "layer"), k("s", "hold: momentary SYM"), k("ADJ", "switch", "layer"),
        ],
    },
    "01-symbol": {
        "title": "Layer 1 — SYMBOL",
        "note": "Neo-style symbols · ~ is emitted as a literal character, not a dead key",
        "keys": [
            none, k("°", "hold: Esc"), k("_"), k("["), k("]"), k("^"),
            k("!"), k("<"), k(">"), k("="), k("&"), none,
            none, k("\\"), k("/", "hold: Ctrl"), k("{", "hold: Alt"), k("}", "hold: GUI"), k("*"),
            k("?"), k("(", "hold: GUI"), k(")", "hold: Alt"), k("-", "hold: Ctrl"), k(":"), none,
            none, k("#"), k("|"), k("$", "hold: €"), k("~", "literal"), k("`"),
            k("+"), k("%"), k("\""), k("'"), k(";"), none,
            k("\\", kind="symbol"), k("$", kind="symbol"), k(":", kind="symbol"),
            k(",", kind="symbol"), k("ß", kind="symbol"), k(".", kind="symbol"),
        ],
    },
    "02-num-nav": {
        "title": "Layer 2 — NUM NAV + MOUSE",
        "note": "The touchpad activates this layer · Precision and Scroll are persistent toggles",
        "keys": [
            none, k("1"), k("2"), k("3"), k("4"), k("5"),
            k("6", kind="numpad"), k("7", kind="numpad"), k("8", kind="numpad"), k("9", kind="numpad"), k("0", kind="numpad"), none,
            none, k("Scroll mode", "tap: toggle · hold: Shift", "layer"), k("←", "hold: Ctrl", "nav"), k("↑", "hold: Alt", "nav"), k("→", "hold: GUI", "nav"), k("Precision", "toggle", "layer"),
            k("Right click", "hold: Middle click", "mouse"), k("4", "hold: GUI", "numpad"), k("5", "hold: Alt", "numpad"), k("6", "hold: Ctrl", "numpad"), k("Space", "hold: Shift", "modifier"), none,
            none, k("Alt + ←", kind="nav"), k("←", kind="nav"), k("↓", kind="nav"), k("→", kind="nav"), k("Alt + →", kind="nav"),
            k("Left click", "holdable for drag", "mouse"), k("1", kind="numpad"), k("2", kind="numpad"), k("3", kind="numpad"), k(".", "hold: ,", "numpad"), none,
            k("Middle click", kind="mouse"), k("Left click", kind="mouse"), k("Right click", kind="mouse"),
            k("+", "hold: *", "numpad"), k("0", kind="numpad"), k("−", "hold: /", "numpad"),
        ],
    },
    "03-adjust": {
        "title": "Layer 3 — ADJUST + MOVE",
        "note": "Tap the outer-right thumb to return to Base · Num/Nav and Symbol are momentary",
        "keys": [
            none, k("Brightness −", kind="media"), k("Brightness +", kind="media"), k("F7"), k("F8"), k("F9"),
            k("Delete", kind="modifier"), k("Previous", kind="media"), k("Play / Pause", kind="media"), k("Next", kind="media"), k("Backspace", kind="modifier"), none,
            none, k("Volume −", "hold: Shift", "media"), k("Volume +", "hold: Ctrl", "media"), k("F4", "hold: Alt"), k("F5", "hold: GUI"), k("F6"),
            k("Esc", kind="modifier"), k("←", "hold: GUI", "nav"), k("↓", "hold: Alt", "nav"), k("↑", "hold: Ctrl", "nav"), k("→", "hold: Shift", "nav"), none,
            none, k("Mute", kind="media"), k("▽", kind="transparent"), k("F1"), k("F2"), k("F3"),
            k("Shift + Tab", kind="modifier"), k("Tab", kind="modifier"), k("Space", kind="modifier"), k("Enter", kind="modifier"), k("Backspace", kind="modifier"), none,
            k("NUM NAV", "momentary", "layer"), k("F11"), k("F12"), k("SYM", "momentary", "layer"), none, k("BASE", "switch", "layer"),
        ],
    },
    "04-system": {
        "title": "Layer 4 — SYSTEM",
        "note": "Momentary only · hold the two outer thumb keys (#36 + #41)",
        "keys": [
            none, k("Clear all BT", kind="danger"), k("BT profile 0", kind="system"), k("BT profile 1", kind="system"), k("BT profile 2", kind="system"), k("BT profile 3", kind="system"),
            k("BT profile 4", kind="system"), k("Bluetooth", kind="system"), k("USB", kind="system"), k("Toggle output", kind="system"), k("Bootloader", kind="danger"), none,
            none, k("Clear BT", kind="danger"), k("Pair profile 0", kind="system"), k("Pair profile 1", kind="system"), k("Pair profile 2", kind="system"), k("Pair profile 3", kind="system"),
            k("Studio unlock", kind="system"), k("Pair profile 4", kind="system"), k("Reset", kind="danger"), k("▽", kind="transparent"), k("▽", kind="transparent"), none,
            none, k("▽", kind="transparent"), k("▽", kind="transparent"), k("▽", kind="transparent"), k("▽", kind="transparent"), k("▽", kind="transparent"),
            k("▽", kind="transparent"), k("▽", kind="transparent"), k("▽", kind="transparent"), k("▽", kind="transparent"), k("▽", kind="transparent"), none,
            none, none, none, none, none, none,
        ],
    },
}

COMBOS = [
    ("Escape", "ä + u", "#27 + #28"),
    ("Up", "c + l", "#8 + #9"),
    ("Page Up", "g + c + l", "#7 + #8 + #9"),
    ("Down", "w + m", "#32 + #33"),
    ("Page Down", "d + w + m", "#31 + #32 + #33"),
    ("Left", "t + r", "#19 + #20"),
    ("Right", "r + n", "#20 + #21"),
    ("Enter", "d + w", "#31 + #32"),
    ("System layer", "outer thumbs", "#36 + #41"),
    ("Backspace", "n + f", "#21 + #22"),
    ("Tab", "a + e", "#14 + #15"),
    ("Shift + Tab", "q + ä", "#26 + #27"),
    ("Copy", "a + o", "#14 + #3"),
    ("Cut", "h + o", "#13 + #3"),
    ("Paste", "i + o", "#16 + #3"),
    ("Undo", ". + o", "#2 + #3"),
    ("Redo", "o + ,", "#3 + #4"),
    ("Delete", "m + j", "#33 + #34"),
]

COLORS = {
    "key": ("#243447", "#3c526b"),
    "modifier": ("#34485f", "#58718d"),
    "layer": ("#174f52", "#2a8588"),
    "symbol": ("#5a3c72", "#9868bd"),
    "numpad": ("#294f75", "#4b85ba"),
    "nav": ("#315c49", "#52936f"),
    "mouse": ("#533e79", "#8567b7"),
    "media": ("#644c2d", "#a77d42"),
    "system": ("#334c6b", "#5e82ad"),
    "danger": ("#713b3b", "#ad5f5f"),
    "transparent": ("#1b2531", "#344252"),
    "none": ("#151d27", "#2b3745"),
}

HIDDEN_POSITIONS = {0, 11, 12, 23, 24, 35}


def key_position(index: int) -> tuple[int, int]:
    if index < 36:
        row, col = divmod(index, 12)
        if col < 6:
            x = 45 + (col - 1) * 108
        else:
            x = 675 + (col - 6) * 108
        return x, 130 + row * 90
    thumb = index - 36
    if thumb < 3:
        return 260 + thumb * 108, 392
    return 675 + (thumb - 3) * 108, 392


def text(svg: list[str], x: float, y: float, value: str, size: int, fill: str, weight: int = 500, anchor: str = "middle") -> None:
    svg.append(f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}">{escape(value)}</text>')


def render_layer(slug: str, layer: dict) -> None:
    width, height = 1260, 515
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">']
    svg.append('<rect width="100%" height="100%" rx="24" fill="#111923"/>')
    text(svg, 45, 52, layer["title"], 28, "#f2f5f8", 700, "start")
    text(svg, 45, 82, layer["note"], 15, "#9fb0c3", 400, "start")
    text(svg, 610, 112, "LEFT", 12, "#66788d", 700)
    text(svg, 650, 112, "RIGHT", 12, "#66788d", 700)

    for index, key in enumerate(layer["keys"]):
        if index in HIDDEN_POSITIONS:
            continue
        x, y = key_position(index)
        w = 100
        h = 68
        fill, stroke = COLORS[key.kind]
        svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="11" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')
        text(svg, x + 8, y + 15, f"#{index}", 9, "#8092a7", 500, "start")
        main_size = 11 if len(key.tap) > 12 else 13 if len(key.tap) > 10 else 18
        main_y = y + (39 if key.hold else 44)
        text(svg, x + w / 2, main_y, key.tap or "—", main_size, "#f5f7fa", 650)
        if key.hold:
            hold_size = 7 if len(key.hold) > 24 else 8 if len(key.hold) > 18 else 10
            text(svg, x + w / 2, y + 57, key.hold, hold_size, "#b7c5d5", 400)

    text(svg, 45, 498, "▽ = transparent · disabled outer matrix positions are omitted", 12, "#718399", 400, "start")
    svg.append('</svg>')
    Path(__file__).with_name(f"{slug}.svg").write_text("\n".join(svg))


def render_combos() -> None:
    width, height = 1160, 650
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">']
    svg.append('<rect width="100%" height="100%" rx="24" fill="#111923"/>')
    text(svg, 42, 52, "Combo reference", 28, "#f2f5f8", 700, "start")
    text(svg, 42, 81, "Labels use the BASE tap action", 15, "#9fb0c3", 400, "start")

    column_width = 550
    for index, (action, keys, positions) in enumerate(COMBOS):
        col = index // 10
        row = index % 10
        x = 42 + col * column_width
        y = 112 + row * 49
        svg.append(f'<rect x="{x}" y="{y}" width="{column_width - 18}" height="40" rx="8" fill="#1b2837"/>')
        text(svg, x + 14, y + 25, action, 14, "#f2f5f8", 650, "start")
        text(svg, x + 180, y + 25, keys, 14, "#b8c7d8", 500, "start")
        text(svg, x + column_width - 34, y + 25, positions, 12, "#718ca8", 500, "end")

    svg.append('</svg>')
    Path(__file__).with_name("05-combos.svg").write_text("\n".join(svg))


for name, data in LAYERS.items():
    render_layer(name, data)
render_combos()
