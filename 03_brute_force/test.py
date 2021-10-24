# netsh wlan show profiles
# netsh wlan show profile router_name
# netsh wlan show profile router_name key=clear


from netmiko import ConnectHandler

connect = 'test'

try:
    connect = ConnectHandler(ip= '192.168.1.210', device_type= 'cisco_ios', username= 'roger', password= '123123')
    # connect = 'testing'
    
except:
    pass

print(connect)