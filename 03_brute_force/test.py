# netsh wlan show profiles
# netsh wlan show profile router_name
# netsh wlan show profile router_name key=clear

# def ssh_connect(ip, user, password, command):
#     client = paramiko.SSHClient()
#     client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     client.connect(ip, username= user, password= password)
#     session = client.get_transport().open_session()
#     if session.active:
#         session.exec_command(command)
#         print(session.recv(1024))
#     return 
# ssh_connect('127.0.0.1', 'test', 'test123', 'id')



# hostname = '127.0.0.1'
# port = 22
# user = 'phil'
# passwd = 'pythoncode'

# try:
#     client = paramiko.SSHClient()
#     client.load_system_host_keys()
#     client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     client.connect(hostname, port= port, username= user, password= passwd)

#     while True:
#         try:
#             cmd = input("$> ")
#             if cmd == "exit": break 
#             stdin, stdout, stderr = client.exec_command(cmd)
#             print(stdout.read().decode())


#         except KeyboardInterrupt:
#             break
#     client.close()


# except Exception as err:
#     print(str(err))

import paramiko


hostname = '127.0.0.1'
port = 22
user = 'test'

try:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, port= port, username= user, password='test123')
    session = client.get_transport().open_session()
    print(session.active)
    print(type(session.active))
    if session.active == 1:
        print('vay aq')
except:
    print('Login Attempt Has Failed')
    
# import numpy as np

# # listA = [11, 18, 19, 21, 29, 46]

# # splits = np.array_split(listA, 3)

# # for array in splits:
# #     print(list(array))


# with open('passwords.txt', 'r') as file:
#     passwords= file.read().split('\n')
    
#     passwords1, passwords2, passwords3, passwords4 = np.array_split(passwords, 4)
#     print(passwords1, passwords2, passwords3, passwords4)    

# flag = False 
# print(flag)


# def test():
#     flag = True
#     return flag

# print(test())


# Python program to illustrate the concept
# of threading
# importing the threading module
# import threading
  
# def print_cube(num):
#     """
#     function to print cube of given num
#     """
#     print("Cube: {}".format(num * num * num))
  
# def print_square(num):
#     """
#     function to print square of given num
#     """
#     print("Square: {}".format(num * num))
  
# if __name__ == "__main__":
#     # creating thread
#     t1 = threading.Thread(target=print_square, args=(10,))
#     t2 = threading.Thread(target=print_cube, args=(10,))
  
#     # starting thread 1
#     t1.start()
#     # starting thread 2
#     t2.start()
  
#     # wait until thread 1 is completely executed
#     t1.join()
#     # wait until thread 2 is completely executed
#     t2.join()
  
#     # both threads completely executed
#     print("Done!")