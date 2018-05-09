from multiprocessing import Process
import socket, argparse

host_ip = "127.0.0.1"
port = 5006










def main():
    send_udp(bytes("woof", 'utf-8'))

def send_udp(payload):
    sock = socket.socket(socket.AF_INET,  # Internet
                         socket.SOCK_DGRAM)  # UDP

    sock.bind((host_ip, port))
    start_sender_process(port,payload)

    while True:
        data, addr = sock.recvfrom(1024)
        print("received payload:", data)

def start_sender_process(port, message):
        p = Process(target=send_message, args=(port,message))
        p.start()
        p.join()


def send_message(port, payload):
    sock = socket.socket(socket.AF_INET,  # Internet
                  socket.SOCK_DGRAM)  # UDP
    sock.sendto(payload, (host_ip, port))

if __name__ == "__main__":
    main()