#!/bin/python3

from scapy.all import IP, UDP, send

def send_udp_packet(source_port, destination_ip, destination_port, message):
    # Create an IP packet with UDP payload
    packet = IP(dst=destination_ip) / UDP(sport=source_port, dport=destination_port) / message

    # Send the packet
    send(packet)

# Example usage
#source_port = 53  # Replace with your desired source port
#destination_ip = '192.168.180.13'  # Replace with the destination IP
#destination_port = 53  # Replace with the destination port
#message = "Hello, UDP!"  # Replace with your message
#for i in range(5000000): 
 #send_udp_packet(source_port, destination_ip, destination_port, message)

