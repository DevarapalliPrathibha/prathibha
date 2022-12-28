from netmiko import ConnectHandler

CSR={
    "device_type": "cisco_ios",

    "ip":"sandbox-iosxe-latest-1.cisco.com",
   # "ip":"sandbox-iosxe-recomm-1.cisco.com",
    "port":22,#netkon--32,,SSH-port 223
    "username":"developer",
    "password":"C1sco12345"
}
net_connect = ConnectHandler(**CSR)
hostname = net_connect.send_command('show run | host')
hostname.split(" ")
hostname, devices, *rest = hostname.split(" ")
print("Backing up" + devices)
filename = "C:/Users/user718/PycharmProjects/pythonProject/devices_12.txt "

showrun = net_connect.send_command('show run')
showvlan = net_connect.send_command('show vlan')
showver = net_connect.send_command('show ver')
log_file = open(filename, "a")
log_file.write(showrun)
log_file.write('\n')
log_file.write(showvlan)
log_file.write('\n')
log_file.write(showver)
log_file.write('\n')
net_connect.disconnect()





