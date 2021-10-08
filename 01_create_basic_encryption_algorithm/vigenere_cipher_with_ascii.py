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


    def remove_mode_layer(self, encrypted_text):
        remove_last_layer = [ (ord(c) - self.last_layer) + self.mod for c in list(encrypted_text) ]
        
        





    def decryption(self):
        pass




if __name__ == "__main__":
    encrypted = Vigenere_Cipher_With_ASCII(input("Message about the be crypted: ")).encryption()
    print(encrypted, len(encrypted))
    

# randomized 
# import random
# random.shuffle(Alphabet)

# print(Alphabet)