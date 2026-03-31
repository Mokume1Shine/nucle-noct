/**
 * JavaScript theme test
 * Comments, classes, methods, async/await, objects, arrays, regex, template strings.
 */

const THEME_NAME = "NucleNoct";
const HEX_COLOR = /^#(?:[0-9a-f]{3}){1,2}$/i;

class PreviewBuilder {
  #items = [];

  add(key, value, active = true) {
    this.#items.push({ key, value, active });
    return this;
  }

  async render() {
    const visible = this.#items.filter((item) => item.active);
    return visible.map((item, index) => `${index}:${item.key}=${item.value}`);
  }
}

async function main() {
  const builder = new PreviewBuilder()
    .add("editor.background", "#002737")
    .add("terminal.ansiMagenta", "#B46CBF")
    .add("invalid.example", "not-a-color", false);

  const lines = await builder.render();
  const normalized = lines.map((line) => (HEX_COLOR.test(line) ? line : `${THEME_NAME}:${line}`));
  console.log(normalized.join("\n"));
}

main().catch((error) => console.error("preview failed", error));
