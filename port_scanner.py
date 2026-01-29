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

    start = time.time()
    open_ports = []

    # Scan each port in our small list
    for port, service in COMMON_PORTS.items():
        if is_port_open(target_ip, port):
            open_ports.append((port, service))
            print(f"OPEN  {port:<5} ({service})")

    end = time.time()

    # Summary
    print("\nSummary")
    print("-------")
    if open_ports:
        print(f"Open ports found: {len(open_ports)}")
    else:
        print("No open ports found in the common list.")

    print(f"Scan time: {end - start:.2f} seconds\n")

    # Simple reminder about ethics
    print("Note: Only scan devices you own or have permission to test.\n")


if __name__ == "__main__":
    main()        