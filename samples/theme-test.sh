#!/usr/bin/env bash

set -euo pipefail

theme_name="NucleNoct"
accent="#00A6C8"
warning="#FE9F2F"

print_preview() {
  local label="$1"
  local color="$2"
  printf '%s => %s\n' "$label" "$color"
}

print_preview "editor.background" "#002737"
print_preview "terminal.ansiMagenta" "#B46CBF"
print_preview "chat.requestCodeBorder" "$accent"
print_preview "warning" "$warning"
