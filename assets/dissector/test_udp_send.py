from multiprocessing import Process
import socket, os

#NOTE: In Windows, Wireshark may not be able to listen on localhost (127.0.0.1), so you need to find your host's non-localhost IP
host_ip = "127.0.0.1"
port = 5006
message="this message should fit an UDP payload of 1024 bytes"

def main():
    send_udp(bytes(message, 'utf-8'))

def send_udp(payload):
    sock = socket.socket(socket.AF_INET,  # Internet
                         socket.SOCK_DGRAM)  # UDP

    sock.bind((host_ip, port))
    start_sender_process(port,payload)

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