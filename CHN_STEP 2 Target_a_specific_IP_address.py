# Target a specific IP address to scan for open ports
import threading
import time
import socket
#...............STEP 2 - Choose the target IP....................
ip_address = input("Enter IP address to scan open ports:")
# function to scan ports and see which ports open
def scan_port(port):
    host_ip = ip_address
    status = ip_address
    # create instance of socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connecting the host ip address and port
    try:
        s.connect((host_ip, port))
        status = True
    except:
        status = False

    if status:
        print("port {} is open".format(port))

start_time = time.time()

for i in range(0, 65000):
    thread = threading.Thread(target=scan_port, args=[i])
    thread.start()
end_time = time.time()
print("Scanning process of all ports took {} seconds".format(end_time - start_time))