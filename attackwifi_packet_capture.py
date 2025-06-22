from scapy.all import sniff, wrpcap

def capture_packets():
    iface = input("Masukkan interface WiFi (mode monitor): ").strip()
    count = input("Jumlah paket yang ingin dicapture (0=tak terbatas): ").strip()
    pcap_file = input("Nama file output (.pcap): ").strip()
    try:
        count = int(count)
        print("[*] Mulai capture... Tekan CTRL+C untuk berhenti.")
        packets = sniff(iface=iface, count=count if count > 0 else 0)
        wrpcap(pcap_file, packets)
        print(f"[+] Paket disimpan ke {pcap_file}")
    except Exception as e:
        print(f"Error: {e}")