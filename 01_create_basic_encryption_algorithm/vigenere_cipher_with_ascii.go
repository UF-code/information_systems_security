package main

import (
	"fmt"
)

func convert_to_ascii(plain_text string) ([]int, int) {
	// ascii := []int{}
	var ascii []int
	for _, x := range plain_text {
		// fmt.Print(int(x), "\n")
		ascii = append(ascii, int(x))
	}

	return ascii, len(ascii)
}

func add_key(ascii []int, key int) []int {
	for i := range ascii {
		ascii[i] += key
	}
	return ascii
}

func add_keyword(ascii []int, keyword string) []int {

}

func convert_to_char(ascii_text []int) ([]string, int) {

	var char []string
	for _, x := range ascii_text {
		// fmt.Print(string(x), "\n")
		char = append(char, string(x))
	}

	return char, len(char)

}

func main() {
	mod := 256

	fmt.Println(mod)
	result_ascii, length_ascii := convert_to_ascii("ugur firat")
	fmt.Print(result_ascii, length_ascii)

	fmt.Print("\n")

	test := add_key(result_ascii, 100)
	fmt.Print(test)

	fmt.Print("\n")

	result_char, length_char := convert_to_char(result_ascii)
	fmt.Print(result_char, length_char)
}
