from scapy.all import rdpcap

def analyze_packets():
    fname = input("Masukkan nama file .pcap: ").strip()
    try:
        packets = rdpcap(fname)
        print(f"[+] Membaca {len(packets)} paket...")
        for i, pkt in enumerate(packets[:10]):
            print(f"--- Paket #{i+1} ---")
            print(pkt.summary())
        print("[*] Analisa lanjutan bisa dikembangkan (filter, protokol, dst).")
    except Exception as e:
        print(f"Error: {e}")
