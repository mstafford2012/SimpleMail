import socket
import ipaddr
import threading
from SimpleMail_lib import *
import time


def main():

    UDP_IP = lib_outward_ip

    BROADCAST = str(ipaddr.IPv4Network(UDP_IP+"/24").broadcast)
    UDP_PORT = 5005

    direct_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    direct_sock.bind((UDP_IP, UDP_PORT))

    broadcast_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    broadcast_sock.bind((BROADCAST, UDP_PORT))

    t1 = threading.Thread(target=receive_messages, args=[direct_sock])
    t2 = threading.Thread(target=receive_messages, args=[broadcast_sock])

    t1.setDaemon(True)
    t2.setDaemon(True)

    t1.start()
    t2.start()

    try:
        while t1.is_alive and t2.is_alive:
            pass

    except KeyboardInterrupt:
        pass


def receive_messages(sock):

    while True:

        data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes

        if addr in get_aliases().values():
            for name, aliased_ip in get_aliases():
                if aliased_ip == addr:
                    sender = name
        else:
            sender = addr

        mail = get_mail()

        item = dict()
        item['From'] = sender
        item['Body'] = data
        item['Read'] = "no"
        mail[time.time()] = item

        set_mail(mail)


main()
