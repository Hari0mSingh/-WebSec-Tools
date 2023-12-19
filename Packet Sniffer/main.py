import socket
from scapy.all import *
from scapy.layers.l2 import Ether

sniffer_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)

sniffer_socket.bind(("0.0.0.0", 0))

sniffer_socket.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

try:
    while True:
        raw_data, addr = sniffer_socket.recvfrom(65535)
        packet = Ether(raw_data)
        print(packet.summary())
except KeyboardInterrupt:
    sniffer_socket.close()
