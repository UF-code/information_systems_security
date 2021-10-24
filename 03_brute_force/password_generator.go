package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	// fmt.Print("Word: ")
	// var word string
	// fmt.Scanln(&word)

	// fmt.Println(word)
	text_list := make([]string, 0)
	scanner := bufio.NewScanner(os.Stdin)

	for scanner.Scan() {
		if scanner.Text() == "q" {
			break
		}

		text_list = append(text_list, scanner.Text())

		fmt.Println("Echo: ", scanner.Text())

	}

	fmt.Println(text_list)
	for i, word := range text_list {
		fmt.Printf("Index: %d Value: %s \n", i, word)
	}
}
