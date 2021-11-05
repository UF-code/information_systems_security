package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func convert_to_ascii(plain_text string) ([]int, int) {
	// ascii := []int{}
	var ascii []int
	for _, x := range plain_text {
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

func generate_keyword_list(length_ascii int, keyword string) []int {
	var extended_keyword_list []string
	counter := 0
	for {
		if len(extended_keyword_list) == length_ascii {
			break
		}
		if counter == len(keyword) {
			counter = 0
		}
		counter += 1
		extended_keyword_list = append(extended_keyword_list, string(keyword[counter-1]))
	}

	ascii, _ := convert_to_ascii(strings.Join(extended_keyword_list, ""))

	return ascii
}

func add_keyword(key_added_ascii []int, keyword_list []int) []int {
	for i := range key_added_ascii {
		key_added_ascii[i] += keyword_list[i]
	}
	return key_added_ascii
}

// ENCRYPTION
func encryption(mod int) string {
	scanner := bufio.NewScanner(os.Stdin)
	fmt.Print("Message about to be encrypted: ")
	scanner.Scan()
	message := scanner.Text()
	// fmt.Printf("%q", message)
	// convert to ascii
	result_ascii, length_ascii := convert_to_ascii(message)
	// fmt.Print(result_ascii, length_ascii)

	// adding key
	fmt.Print("Key: ")
	scanner.Scan()
	key, _ := strconv.ParseInt(scanner.Text(), 10, 64)
	key_added_ascii := add_key(result_ascii, int(key))

	fmt.Print("Keyword: ")
	scanner.Scan()
	keyword := scanner.Text()
	keyword_list := generate_keyword_list(length_ascii, keyword)

	encrypted_ascii := add_keyword(key_added_ascii, keyword_list)

	var encrypted_message []string
	for i := range encrypted_ascii {
		encrypted_ascii[i] += mod
		encrypted_message = append(encrypted_message, string(encrypted_ascii[i]))
	}

	return strings.Join(encrypted_message, "")

}

// DECRYPTION
func convert_to_char(ascii_text []int) ([]string, int) {
	var char []string
	for _, x := range ascii_text {
		// fmt.Print(string(x), "\n")
		char = append(char, string(x))
	}

	return char, len(char)

}

func remove_mod_layer(encrypted_message string, mod int) ([]int, int) {
	var mod_layer_removed []int

	for _, x := range encrypted_message {
		// fmt.Println(int(x) + 1)
		mod_layer_removed = append(mod_layer_removed, int(x)-mod)
	}

	return mod_layer_removed, len(mod_layer_removed)
}

func remove_key(ascii []int, key int) []int {
	for i := range ascii {
		ascii[i] -= key
	}
	return ascii
}

func remove_keyword(key_added_ascii []int, keyword_list []int) []int {
	for i := range key_added_ascii {
		key_added_ascii[i] -= keyword_list[i]
	}
	return key_added_ascii
}

func decryption(mod int) {
	scanner := bufio.NewScanner(os.Stdin)
	fmt.Print("Message about to be decrypted: ")
	scanner.Scan()
	encrypted_message := scanner.Text()

	mod_layer_removed, length_of_mod_layer := remove_mod_layer(encrypted_message, mod)

}

func main() {
	mod := 256
	test := encryption(mod)
	fmt.Println(test)

	// decryption(mod)
}
