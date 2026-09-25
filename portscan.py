#!/usr/bin/env python3
"""Quick TCP port scanner. For your own lab only."""
import socket
import sys
from concurrent.futures import ThreadPoolExecutor

def scan(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    try:
        s.connect((host, port))
        return port
    except Exception:
        return None
    finally:
        s.close()

def main():
    if len(sys.argv) < 2:
        print("usage: portscan.py <host> [start] [end]")
        sys.exit(1)
    host = sys.argv[1]
    start = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    end = int(sys.argv[3]) if len(sys.argv) > 3 else 1024

    with ThreadPoolExecutor(max_workers=200) as ex:
        results = ex.map(lambda p: scan(host, p), range(start, end + 1))

    for port in results:
        if port:
            print(f"[+] {port} open")

if __name__ == "__main__":
    main()
