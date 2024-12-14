import socket

def scan_ports(target, ports):
    print(f"Scanning {target} for open ports...")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        
        if result == 0:
            print(f"Port {port} is open.")
        else:
            print(f"Port {port} is closed.")
        sock.close()

# Example usage
target = input("Enter the target IP address: ")
ports = [22, 80, 443, 8080]  # You can add more ports here
scan_ports(target, ports)
