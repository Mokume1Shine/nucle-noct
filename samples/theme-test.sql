SELECT
  'NucleNoct' AS theme_name,
  '#002737' AS editor_background,
  '#00A6C8' AS json_key,
  '#B46CBF' AS terminal_magenta,
  '#FE9F2F' AS accent_signal
FROM theme_preview
WHERE enabled = TRUE
ORDER BY theme_name ASC;
