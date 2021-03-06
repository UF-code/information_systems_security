import sys

class Vigenere_Cipher_With_ASCII:
    def __init__(self):
        self.mod = 140
        self.last_layer = 194

    # Converting every single characther into their ascii code
    def ascii_layer(self, message):
        message_text = list(message.replace(" ", ""))
        numerical_list = [ord(c) for c in message_text]
        return numerical_list

    # Adding a numerical key into each ascii lists item
    def key_layer(self, key, numerical_list):
        key_added_list = [n + key for n in numerical_list]
        return key_added_list
    
    # Extending a keyword list to match lenght of the message
    # Converting every single characther into their ascii code
    def keyword_layer(self, keyword, ascii_list):
        formatted_keyword_list = list(keyword.replace(" ", ""))
        extended_keyword_list = []

        counter=0
        while True:
            if len(extended_keyword_list) == len(ascii_list):
                break
            if counter == len(formatted_keyword_list):
                counter=0
            extended_keyword_list.append(formatted_keyword_list[counter])
            counter+=1
        
        extended_ascii_keyword_list = [ord(c) for c in extended_keyword_list]
        return extended_ascii_keyword_list
    
    # Adding key added message and extended keyword list together
    # Taking a mod of that combined list
    # Converting every single ascii code into their Charachter Value
    def mod_layer(self, key_added_list, extended_keyword_list):
        modded_list = [ (key_added_list[i] + extended_keyword_list[i]) % self.mod for i in range(len(key_added_list)) ]
        result_text = [ chr( n + self.last_layer ) for n in modded_list ]
        return ''.join(result_text)


    def encryption(self):
        ascii_list   = self.ascii_layer(input("Message about to be crypted: "))
        key_list     = self.key_layer(int(input("Key: ")), ascii_list)
        keyword_list = self.keyword_layer(input("Keyword: "), ascii_list)
        mod_layer    = self.mod_layer(key_list, keyword_list)
        
        print(f"Encrypted Text: {mod_layer}")
        return mod_layer


    # removing mod & last layer
    def remove_mod_layer(self, encrypted_text):
        mod_layer_removed = [ (ord(c) - self.last_layer) + self.mod for c in list(encrypted_text) ]
        return mod_layer_removed

    # removing keyword layer
    def remove_keyword_layer(self, mod_layer_removed, extended_keyword_list):
        extended_keyword_removed = [ (mod_layer_removed[i] - extended_keyword_list[i]) for i in range(len(mod_layer_removed)) ]
        return extended_keyword_removed

    # removing key layer
    def remove_key_layer(self, extended_keyword_removed, key):
        key_layer_removed = [ n - key for n in extended_keyword_removed ]
        return key_layer_removed

    # removing ascii layer
    def remove_ascii_layer(self, key_layer_removed):
        ascii_layer_removed = [ chr(n) for n in key_layer_removed ]
        return ascii_layer_removed

    # Decrypting the encrypted message
    def decryption(self):
        mod_layer_removed = self.remove_mod_layer(input('Encrypted message about to be decrypted: '))
        extended_keyword_list = self.keyword_layer(input("Keyword: "), mod_layer_removed)
        keyword_layer_removed = self.remove_keyword_layer(mod_layer_removed, extended_keyword_list)
        key_layer_removed = self.remove_key_layer(keyword_layer_removed, int(input("Key: ")))
        ascii_layer_removed = self.remove_ascii_layer(key_layer_removed)
        decrypted_text = ''.join(ascii_layer_removed)

        print(decrypted_text)
        return decrypted_text
        

if __name__ == "__main__":
    # if system argument is "enc" Encryption & if you wanna chose decryption you have to specify system arg as 'dec'
    Vigenere_Cipher_With_ASCII().decryption() if sys.argv[1] == 'dec' else Vigenere_Cipher_With_ASCII().encryption() 
