import socket
import threading
import os
from colorama import Fore as f


def is_port_open(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)  
            sock.connect((ip, port))
        return True
    except (socket.timeout, ConnectionRefusedError):
        return False

def check_ports(ip, start_port, end_port):
    for port in range(start_port, end_port + 1):
        if is_port_open(ip, port):
            print(f.GREEN + f"Port {port} is open on {ip}")


if __name__ == "__main__":
    ip = input(f.WHITE + "Enter the IP address you want to check: ")
    print('Checking..')
    start_port = 1
    end_port = 9999


    chunk_size = 100
    for chunk_start in range(start_port, end_port + 1, chunk_size):
        chunk_end = min(chunk_start + chunk_size - 1, end_port)
        thread = threading.Thread(target=check_ports, args=(ip, chunk_start, chunk_end))
        thread.start()
