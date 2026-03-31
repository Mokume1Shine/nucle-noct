/**
 * NucleNoct preview scene
 * Dim waterline, quiet signals, async traces, and phosphor-like accents.
 */

const THEME_NAME = "NucleNoct";
const HEX_COLOR = /^#(?:[0-9a-f]{3}){1,2}$/i;

class SignalLantern {
  #signals = [];

  add(key, value, active = true) {
    this.#signals.push({ key, value, active });
    return this;
  }

  async render() {
    const visible = this.#signals.filter((signal) => signal.active);
    return visible.map((signal, index) => `${index}:${signal.key}=${signal.value}`);
  }
}

async function main() {
  const lantern = new SignalLantern()
    .add("editor.background", "#002737")
    .add("terminal.ansiMagenta", "#B46CBF")
    .add("silent.current", "not-a-color", false);

  const lines = await lantern.render();
  const normalized = lines.map((line) => (HEX_COLOR.test(line) ? line : `${THEME_NAME}:${line}`));
  console.log(normalized.join("\n"));
}

main().catch((error) => console.error("signal lost", error));
