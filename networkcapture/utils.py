
from scapy.all import sniff, IP
from .models import NetworkCapture

def packet_callback(packet):
    if IP in packet:
        protocol = packet.proto
        source_ip = packet[IP].src
        destination_ip = packet[IP].dst
        length = len(packet)
        
        NetworkCapture.objects.create(
            protocol=protocol,
            source_ip=source_ip,
            destination_ip=destination_ip,
            length=length
        )

def capture_traffic():
    sniff(prn=packet_callback, count=10)  # Capture 10 packets for example

