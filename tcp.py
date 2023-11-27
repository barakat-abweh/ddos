#!/bin/python3

from scapy.all import IP, UDP, send

def send_udp_packet(source_port, destination_ip, destination_port, message):
    # Create an IP packet with UDP payload
    packet = IP(dst=destination_ip) / UDP(sport=source_port, dport=destination_port) / message

    # Send the packet
    send(packet)
#fghjkl;'lkjkl;kjhgj
