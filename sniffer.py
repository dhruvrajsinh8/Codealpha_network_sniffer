from scapy.all import sniff

def packet_callback(packet):
    print("\nPacket Summary:")
    if packet.haslayer("IP"):
        print(f"Source IP: {packet['IP'].src}")
        print(f"Destination IP: {packet['IP'].dst}")
        print(f"Protocol: {packet['IP'].proto}")

        if packet.haslayer("TCP"):
            print(f"TCP Source Port: {packet['TCP'].sport}")
            print(f"TCP Destination Port: {packet['TCP'].dport}")
            print(f"Payload: {packet['TCP'].payload}")
        elif packet.haslayer("UDP"):
            print(f"UDP Source Port: {packet['UDP'].sport}")
            print(f"UDP Destination Port: {packet['UDP'].dport}")
            print(f"Payload: {packet['UDP'].payload}")
        else:
            print("Non-TCP/UDP Layer, raw data:")
            print(packet.show())

sniff(prn=packet_callback, count=10, filter="ip", store=0)
