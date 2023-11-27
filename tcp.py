#!/bin/python3

from scapy.all import IP, TCP, send

def send_custom_tcp_packet(source_port, destination_ip, destination_port, flags, message):
    # Create an IP packet with TCP payload and custom flags
    packet = IP(dst=destination_ip) / TCP(sport=source_port, dport=destination_port, flags=flags) / message

    # Send the packet
    send(packet)
