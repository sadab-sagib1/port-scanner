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