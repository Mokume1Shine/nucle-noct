package main

import (
	"fmt"
	"regexp"
)

type PaletteToken struct {
	Key    string
	Value  string
	Active bool
}

func main() {
	hexColor := regexp.MustCompile(`^#(?:[0-9a-fA-F]{3}){1,2}$`)
	tokens := []PaletteToken{
		{Key: "editor.background", Value: "#002737", Active: true},
		{Key: "terminal.ansiMagenta", Value: "#B46CBF", Active: true},
		{Key: "chat.requestCodeBorder", Value: "#00A6C8", Active: true},
	}

	for _, token := range tokens {
		if token.Active && hexColor.MatchString(token.Value) {
			fmt.Printf("%s => %s\n", token.Key, token.Value)
		}
	}
}
