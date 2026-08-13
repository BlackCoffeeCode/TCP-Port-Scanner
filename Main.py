import socket
import threading

host = socket.gethostbyname(input("Enter host to scan: "))

start = int(input("Enter starting port: "))
end = int(input("Enter ending port: "))

print("\n" + "=" * 40)
print("        PYTHON PORT SCANNER")
print("=" * 40)
print(f"Target : {host}")
print(f"Ports  : {start}-{end}")
print("=" * 40)


def scan(port):
    s = socket.socket()
    s.settimeout(1)
    result = s.connect_ex((host, port))
    if result == 0:
        print(f"[OPEN]   Port {port}")
    s.close()


for i in range(start, end + 1):
    t = threading.Thread(target=scan, args=(i,))
    t.start()