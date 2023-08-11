from scapy.all import *


# Callback function for each captured packet
def handle_packet(pkt):
    print(hexdump(pkt))


# Start capturing packets
sniff(iface="Ethernet", filter="tcp", prn=handle_packet)

