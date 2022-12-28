"""
from getmac import get_mac_address as gma
print(gma())
"""
import uuid
#printing the value of unique mac
#address using uuid and getnode() function
print(hex(uuid.getnode()))
#uuid - package/library class
#uuid - random objects : 128_bits[random objects/mac addresses]
print("the mac address in formated way is:",end="")
print(':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) #ele - data container,0x - representation, ff - range,8bits,6parts
    for ele in range(0,8*6,8)][::-1]))# -1 : negative indexing