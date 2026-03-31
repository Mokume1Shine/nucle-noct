/**
 * NucleNoct color theme test file
 * Check comments, keywords, operators, types, functions, methods,
 * strings, template expressions, regex, numbers, readonly values,
 * enums, properties, parameters, and markdown-like text in strings.
 */

type ThemeMode = "void" | "signal" | "frost";

interface PaletteToken {
  readonly key: string;
  value: string;
  active?: boolean;
  tags: string[];
}

enum Severity {
  Info = 1,
  Warning = 2,
  Error = 3,
}

const THEME_NAME = "NucleNoct";
const MAX_PREVIEW_COUNT = 5;
const HEX_COLOR = /^#(?:[0-9a-fA-F]{3}){1,2}$/;

class ThemePreviewer {
  constructor(
    private readonly title: string,
    private readonly tokens: PaletteToken[],
  ) {}

  get visibleTokens(): PaletteToken[] {
    return this.tokens.filter((token) => token.active !== false);
  }

  formatLabel(mode: ThemeMode, count = 0): string {
    return `${this.title}:${mode}:${count.toString().padStart(2, "0")}`;
  }

  print(token: PaletteToken, severity: Severity): string {
    const suffix = severity === Severity.Error ? "!" : ".";
    return `${token.key} => ${token.value}${suffix}`;
  }
}

function normalizeToken(token: PaletteToken, mode: ThemeMode): PaletteToken {
  const fallback =
    mode === "signal" ? "#00A6C8" : mode === "frost" ? "#E4F4F7" : "#002737";

  return {
    ...token,
    value: HEX_COLOR.test(token.value) ? token.value : fallback,
    tags: [...new Set(token.tags)].sort(),
  };
}

function buildPreview(mode: ThemeMode, input: PaletteToken[]): string[] {
  const previewer = new ThemePreviewer(THEME_NAME, input);
  const items = previewer.visibleTokens.slice(0, MAX_PREVIEW_COUNT);

  return items.map((token, index) => {
    const normalized = normalizeToken(token, mode);
    const level =
      index % 3 === 0
        ? Severity.Info
        : index % 3 === 1
          ? Severity.Warning
          : Severity.Error;

    return `${previewer.formatLabel(mode, index)} ${previewer.print(normalized, level)}`;
  });
}

const previewTokens: PaletteToken[] = [
  { key: "editor.background", value: "#002737", active: true, tags: ["base", "editor"] },
  { key: "terminal.ansiMagenta", value: "#B46CBF", active: true, tags: ["terminal", "ansi"] },
  { key: "terminal.ansiBrightMagenta", value: "#D59AE0", active: true, tags: ["terminal", "ansi"] },
  { key: "chat.requestCodeBorder", value: "#00A6C8", active: true, tags: ["chat", "accent"] },
  { key: "textPreformat.foreground", value: "#FEB656", active: true, tags: ["text", "warm"] },
  { key: "invalid.example", value: "not-a-color", active: false, tags: ["invalid"] },
];

const previews = buildPreview("signal", previewTokens);

for (const line of previews) {
  console.log(line);
}

const nested = {
  palette: {
    base: "#002737",
    panel: "#0C3444",
    border: "#355C68",
    key: "#00A6C8",
    string: "#E4F4F7",
  },
  notes: [
    "Headings should stand out.",
    "JSON keys should be brighter than string values.",
    "Magenta should look magenta in the terminal.",
  ],
};

console.log(nested.palette.base, nested.notes.join(" / "));
