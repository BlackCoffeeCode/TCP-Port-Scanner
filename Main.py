import socket, threading
host=socket.gethostbyname(input ("Enter host to scan: "))
start=1
end=1000

def scan(port):
    s = socket. socket()
    s.settimeout(3)
    result = s.connect_ex((host,port))
    if result==0:
        print ("port open", port)
    s. close ()
for i in range(start,end+1):
     t=threading.Thread(target=scan, args= (i, ))
     t.start ()