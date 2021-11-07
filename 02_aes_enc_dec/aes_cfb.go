package main

import (
	"bufio"
	"crypto/aes"
	"crypto/cipher"
	"encoding/base64"
	"fmt"
	"os"
)

func encryption(message, secret_key, initial_vector string) string {
	block, _ := aes.NewCipher([]byte(secret_key))
	plain_text := []byte(message)
	cfb := cipher.NewCFBEncrypter(block, []byte(initial_vector))

	cipher_text := make([]byte, len(plain_text))
	cfb.XORKeyStream(cipher_text, plain_text)

	return base64.StdEncoding.EncodeToString(cipher_text)
}

func get_input() (string, string, string) {
	scanner := bufio.NewScanner(os.Stdin)

	// message about to be decrypted or encrypted
	var message string
	if os.Args[1] == "dec" {
		fmt.Print("Message About to be Decrypted: ")
		scanner.Scan()
		message = scanner.Text()
	} else {
		fmt.Print("Message About to be Encrypted: ")
		scanner.Scan()
		message = scanner.Text()
	}

	// secret key
	fmt.Print("Secret Key: ")
	scanner.Scan()
	secret_key := scanner.Text()

	// initial vector
	fmt.Print("Initial Vector: ")
	scanner.Scan()
	initial_vector := scanner.Text()

	return message, secret_key, initial_vector
}

func main() {
	if os.Args[1] == "dec" {
		message, secret_key, initial_vector := get_input()
		fmt.Println(decryption(message, secret_key, initial_vector))
	} else {
		message, secret_key, initial_vector := get_input()
		fmt.Println(encryption(message, secret_key, initial_vector))
	}
}
