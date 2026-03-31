import java.util.List;

public final class ThemeTest {
    private record PaletteToken(String key, String value, boolean active) {}

    public static void main(String[] args) {
        List<PaletteToken> tokens = List.of(
            new PaletteToken("editor.background", "#002737", true),
            new PaletteToken("terminal.ansiMagenta", "#B46CBF", true),
            new PaletteToken("chat.requestCodeBorder", "#00A6C8", true)
        );

        for (PaletteToken token : tokens) {
            if (token.active()) {
                System.out.println(token.key() + " => " + token.value());
            }
        }
    }
}
