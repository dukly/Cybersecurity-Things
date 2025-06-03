import socket
import concurrent.futures
from typing import List

def scan_port(host: str, port: int, timeout: float = 1.0) -> bool:
    """Check if a port is open and identify the service."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            if s.connect_ex((host, port)) == 0:
                try:
                    service = socket.getservbyport(port)
                except:
                    service = "unknown"
                print(f"✅ [OPEN] Port {port}: {service}")
                return True
    except Exception as e:
        print(f"⚠️  Error scanning port {port}: {e}")
    return False

def scan_ports(host: str, ports: List[int], max_threads: int = 100) -> None:
    """Multi-threaded port scanner."""
    print(f"🚀 Scanning {host}...")
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = [executor.submit(scan_port, host, port) for port in ports]
        concurrent.futures.wait(futures)

if __name__ == "__main__":
    target = input("Enter target IP/hostname: ")
    port_range = input("Enter ports (e.g., '80,443' or '1-1000'): ")
    
    if "-" in port_range:
        start, end = map(int, port_range.split("-"))
        ports = list(range(start, end + 1))
    else:
        ports = [int(p) for p in port_range.split(",")]
    
    scan_ports(target, ports)