#[derive(Debug)]
struct PaletteToken<'a> {
    key: &'a str,
    value: &'a str,
    active: bool,
}

fn main() {
    let tokens = [
        PaletteToken { key: "editor.background", value: "#002737", active: true },
        PaletteToken { key: "terminal.ansiMagenta", value: "#B46CBF", active: true },
        PaletteToken { key: "chat.requestCodeBorder", value: "#00A6C8", active: true },
    ];

    for token in tokens.iter().filter(|token| token.active) {
        println!("{} => {}", token.key, token.value);
    }
}
