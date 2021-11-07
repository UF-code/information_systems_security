package main

import (
	"crypto/aes"
	"crypto/cipher"
	"encoding/base64"
	"fmt"
)

var iv = []byte("crGTopEfBGXE1k1x")
var secretKey string = "wEgDCNvhccofPTkFt9zUdDgZDIVdGC9L"

func encodeBase64(b []byte) string {
	return base64.StdEncoding.EncodeToString(b)
}
func decodeBase64(s string) []byte {
	data, err := base64.StdEncoding.DecodeString(s)
	if err != nil {
		panic(err)
	}
	return data
}
func Encrypt(text, secretKey string) (string, error) {
	block, err := aes.NewCipher([]byte(secretKey))
	if err != nil {
		return "", err
	}
	plaintext := []byte(text)
	cfb := cipher.NewCFBEncrypter(block, iv)

	ciphertext := make([]byte, len(plaintext))
	cfb.XORKeyStream(ciphertext, plaintext)

	return encodeBase64(ciphertext), nil
}

func Decrypt(text, secretKey string) (string, error) {
	block, err := aes.NewCipher([]byte(secretKey))
	if err != nil {
		return "", err
	}
	ciphertext := decodeBase64(text)
	cfb := cipher.NewCFBDecrypter(block, iv)
	plaintext := make([]byte, len(ciphertext))
	cfb.XORKeyStream(plaintext, ciphertext)

	return string(plaintext), nil
}

func main() {

	// enc
	phrase := "http://yaz.tf.firat.edu.tr/tr"
	enc_text, err := Encrypt(phrase, secretKey)
	if err != nil {
		fmt.Println("Error reason: ", err)
	}
	fmt.Println("Encrypted Text: ", enc_text)

	// dec
	dec_text, err := Decrypt(enc_text, secretKey)
	if err != nil {
		fmt.Println("Error reason: ", err)
	}
	fmt.Println("Decrypted Text: ", dec_text)
}
