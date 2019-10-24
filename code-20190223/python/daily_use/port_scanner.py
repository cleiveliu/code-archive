# source:https://stackoverflow.com/questions/26174743/making-a-fast-port-scanner
# This script runs on Python 3
import socket
import threading


def TCP_connect(ip, port_number, delay, output):
    TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    TCPsock.settimeout(delay)
    try:
        TCPsock.connect((ip, port_number))
        output[port_number] = 'Listening'
    except BaseException:
        output[port_number] = ''


def scan_ports(host_ip, delay):

    threads = []        # To run TCP_connect concurrently
    output = {}         # For printing purposes

    # Spawning threads to scan ports
    for i in range(10000):
        t = threading.Thread(
            target=TCP_connect, args=(
                host_ip, i, delay, output))
        threads.append(t)

    # Starting threads
    for i in range(10000):
        threads[i].start()

    # Locking the main thread until all threads complete
    for i in range(10000):
        threads[i].join()

    # Printing listening ports from small to large
    for i in range(10000):
        if output[i] == 'Listening':
            print(str(i) + ': ' + output[i])


def main():
    host_ip = "139.180.195.47"  # input("Enter host IP: ")
    # int(input("How many seconds the socket is going to wait until timeout: "))
    delay = 0.4
    scan_ports(host_ip, delay)


if __name__ == "__main__":
    main()
