# codealpha_Network Sniffer

This is a simple network sniffer built using Python and Scapy. The sniffer captures network packets, analyzes their content, and displays useful information like source/destination IPs, protocols, ports, and payloads. It can also save the captured packets to a `.pcap` file for further analysis.

## Features
- Capture network packets in real-time
- Display packet summary: IPs, protocols, ports, payloads
- Save packets to a `.pcap` file for later analysis (e.g., in Wireshark)
- Supports filtering packets by protocol (TCP, UDP, etc.)
- Command-line arguments for flexibility (interface, count, filter)

## Requirements
- Python 3.x
- Scapy

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/network-sniffer.git
   cd network-sniffer
   ```

2. Install dependencies using `pipx` or `virtualenv`:
   
   ```bash
   pipx install scapy
   ```

3. Run the sniffer script:

   ```bash
   python3 sniffer.py
   ```

## Usage

- Capture packets for 10 packets:

  ```bash
  python3 sniffer.py --count 10
  ```

- Capture packets indefinitely:

  ```bash
  python3 sniffer.py
  ```

## License

This project is licensed under the MIT License.
