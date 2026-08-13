import socket
import threading

host = socket.gethostbyname(input("Enter host to scan: "))

start = int(input("Enter starting port: "))
end = int(input("Enter ending port: "))

print("\n" + "=" * 50)
print("             PYTHON PORT SCANNER")
print("=" * 50)
print(f"Target : {host}")
print(f"Ports  : {start}-{end}")
print("=" * 50)


services = {
    20: "FTP-Data",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    5900: "VNC",
    8080: "HTTP-Proxy"
}


def scan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    result = s.connect_ex((host, port))

    if result == 0:
        service = services.get(port, "Unknown")
        print(f"[OPEN]   {port:<6} {service}")

    s.close()


print(f"{'STATUS':<10}{'PORT':<8}SERVICE")
print("-" * 30)

for port in range(start, end + 1):
    t = threading.Thread(target=scan, args=(port,))
    t.start()