# NucleNoct Theme Test

このファイルは Markdown の見え方確認用です。

## Headings

通常テキスト、**bold**、*italic*、`inline code`、[link text](https://example.com) を並べています。

## List

- editor background
- command palette hover
- JSON key/value contrast
- terminal magenta

## Quote

> Dream Disrupter Light の印象に近いか確認する。

## Code Block: JSON

```json
{
  "editor.background": "#002737",
  "input.background": "#072A36",
  "terminal.ansiMagenta": "#B46CBF",
  "terminal.ansiBrightMagenta": "#D59AE0",
  "json.key": "#00A6C8",
  "json.string": "#E4F4F7"
}
```

## Code Block: TypeScript

```ts
const themeName = "NucleNoct";
const accent = "#FE9F2F";
const regex = /^#(?:[0-9a-fA-F]{3}){1,2}$/;

function preview(label: string, enabled = true): string {
  return enabled ? `${label}:ready` : `${label}:off`;
}
```
