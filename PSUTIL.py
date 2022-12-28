import psutil  #low-level n/w interactions(one or multiple "nic's")
result1 = psutil.cpu_times()
result2 = psutil.cpu_stats()
result3 = psutil.cpu_freq()
result4 = psutil.disk_partitions()  #local machine/vm/storage unit
result5 = psutil.net_io_counters(pernic=True) # pernic=true = false-->collect the snetio info from all the nic's together and display
print(result1)
print("******************")
print(result2)
print("******************")
print(result3)
print("******************")
print(result4)
print("******************")
print(result5)
print("******************")
#data comes in the form of dictionary (eg:lan1,lan2,wi-fi,;oopback_pseudo),1 packet = 255 bytes
network_stats = psutil.net_io_counters(pernic=False) #removing = false
bytes_sent = getattr(network_stats,'bytes_sent')
bytes_recv = getattr(network_stats,'bytes_recv')
print(bytes_sent)
print(bytes_recv)
#print("bytes sent = {0} | bytes received = {1} ".format(bytes_sent,bytes_recv)) .formart = string




