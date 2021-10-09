class Vigenere_Cipher_With_ASCII:
    def __init__(self, message):
        self.message = list(message.replace(" ", ""))
        self.mod = 140
        self.last_layer = 194

    # Converting every single characther into their ascii code
    def ascii_layer(self):
        numerical_list = [ord(c) for c in self.message]
        return numerical_list

    # Adding a numerical key into each ascii lists item
    def key_layer(self, key, numerical_list):
        key_added_list = [n + key for n in numerical_list]
        return key_added_list
    
    # Extending a keyword list to match lenght of the message
    # Converting every single characther into their ascii code
    def keyword_layer(self, keyword):
        formatted_keyword_list = list(keyword.replace(" ", ""))
        extended_keyword_list = []

        counter=0
        while True:
            if len(extended_keyword_list) == len(self.message):
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
        ascii_list   = self.ascii_layer()
        key_list     = self.key_layer(int(input("Key: ")), ascii_list)
        keyword_list = self.keyword_layer(input("Keyword: "))
        mod_layer    = self.mod_layer(key_list, keyword_list)

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

    def remove_ascii_layer(self):
        pass

    # Decrypting the encrypted message
    def decryption(self, encrypted_text, extended_keyword_list, key):
        remove_last_layer_mod = [ (ord(c) - self.last_layer) + self.mod for c in list(encrypted_text) ]
        remove_extended_keyword = [ (remove_last_layer_mod[i] - extended_keyword_list[i]) for i in range(len(remove_last_layer_mod)) ]
        remove_key_layer = [ n - key for n in remove_extended_keyword ]
        convert_ascii_to_char = [ chr(n) for n in remove_key_layer ]
        
        return convert_ascii_to_char


if __name__ == "__main__":
    encrypted = Vigenere_Cipher_With_ASCII(input("Message about to be crypted: ")).encryption()
    print(encrypted, len(encrypted))
    

