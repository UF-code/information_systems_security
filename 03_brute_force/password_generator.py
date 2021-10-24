from itertools import product

def password_generator(length):
    char_list = []
    
    word = input("Word: ")
    while word != 'q':
        for char in list(word):
            if char not in char_list:
                char_list.append(char)
        word = input("Word: ")
    
    chars = ''.join(char_list)

    print(chars)

    product_list = product(chars, repeat=int(length))

    with open('passwords.txt', 'w') as file:
        for password in product_list:
            file.write(''.join(password))
            file.write('\n')

if __name__ == "__main__":
    password_generator(input("Password Length: "))