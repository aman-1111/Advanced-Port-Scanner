import socket
import threading
import argparse

print("🔍 Advanced Port Scanner by Aman Chaurasia")

# Lock for clean terminal output
print_lock = threading.Lock()

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        with print_lock:
            if result == 0:
                print(f"[OPEN] Port {port}")
        sock.close()
    except:
        pass

def main():
    parser = argparse.ArgumentParser(description="Advanced Port Scanner")
    parser.add_argument("target", help="Target IP address or hostname")
    parser.add_argument("-s", "--start", type=int, default=1, help="Start port (default: 1)")
    parser.add_argument("-e", "--end", type=int, default=1024, help="End port (default: 1024)")
    args = parser.parse_args()

    target_ip = socket.gethostbyname(args.target)
    print(f"\nScanning target: {target_ip}")
    print(f"Scanning ports: {args.start} to {args.end}\n")

    threads = []
    for port in range(args.start, args.end + 1):
        t = threading.Thread(target=scan_port, args=(target_ip, port))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\n✅ Scan Completed!")

if __name__ == "__main__":
    main()
