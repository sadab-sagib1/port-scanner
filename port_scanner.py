# Simple TCP Port Scanner
# Usage:
#   python3 port_scanner.py google.com
#   python3 port_scanner.py 192.168.1.1

import socket
import sys
import time

# A small list of common ports (safe + practical for learning)
COMMON_PORTS = {
    20: "FTP data",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3389: "RDP",
}

def is_port_open(target_ip: str, port: int, timeout: float = 0.5) -> bool:
    # Try to connect to (IP, port). If connect works, port is open.
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        result = s.connect_ex((target_ip, port))  # 0 means success
        s.close()
        return result == 0
    except OSError:
        return False
    
def main():
    # Check user input
    if len(sys.argv) != 2:
        print("Usage: python3 port_scanner.py <hostname-or-ip>")
        print("Example: python3 port_scanner.py google.com")
        return
    target = sys.argv[1]

    # Convert hostname -> IP
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("Could not resolve that hostname. Check spelling.")
        return
    
    print("\nSimple TCP Port Scanner")
    print("-----------------------")
    print("Target:", target)
    print("IP:    ", target_ip)
    print("\nScanning common ports...\n")