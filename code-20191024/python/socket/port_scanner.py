import socket
from threading import Thread








def connect(ip, port, ret):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(3)
    try:
        s.connect((ip, port))
        ret[port] = True
    except:
        pass



def main():
    ret = {}
    tasks = []
    ip = "45.32.144.194"

    for i in range(20_000):
        tasks.append(Thread(target=connect, args=(ip,i+1, ret)))


    for i in range(len(tasks)):
        tasks[i].start()

    for i in range(len(tasks)):
        tasks[i].join()
    print(ret)
    print(ip)
    for port in ret:
        print(f"{port} is lll***")

if __name__ == "__main__":
    main()