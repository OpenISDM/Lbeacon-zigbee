"""
This is a remote client (in the same local network) to connect to Xbee gateway. 
"""
import socket, sys

# Local IP address of Gateway
host = '192.168.1.176'
port = 1234

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    sys.stderr.write("[ERROR] %s\n" % msg[1])
    sys.exit(1)
 
try:
    sock.connect((host, port))
except socket.error, msg:
    sys.stderr.write("[ERROR] %s\n" % msg[1])
    exit(1)
   

# dict format for transmission data in Zigbee network
# broacast address test
# dest_addr = '\x00\x00\x00\x00\x00\x00\xFF\xFF'
# specific dest
dest_addr = '\x00\x13\xA2\x00\x40\xE7\xDA\x61'

# which direction, table saved in beacon-- by Jane
data = "2"
# data = "Turn left and ..."
print dest_addr
pack_XBee = { 'dest_addr' : dest_addr, 'data' : data }

# print pack_XBee['dest_addr'] 
sock.send(str(pack_XBee))

print sock.recv(1024)
sock.close()