import socket

def scan_ports(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(1)
        sock.connect((ipaddress, port))
        print("[+] Port Opened", port)
        sock.close()
    except:
        pass

def scan(target, ports):
    print("\nStart scanning for:", target)
    for port in range(1, ports + 1):
        scan_ports(target, port)

target = input("Enter target: ")
ports = int(input("Enter number of ports: "))
scan(target, ports)
