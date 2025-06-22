from utils import select_interface
from wifi_scan import scan_wifi
from wifi_attack import attack_menu
from packet_capture import capture_packets
from packet_analyze import analyze_packets

def main_menu():
    iface = None
    while not iface:
        iface = select_interface()
    while True:
        print("""
   ___      _        _        _      _  __ _       
  / _ \\__ _| |_ __ _| | _____| |__  (_)/ _| | _____
 | | | / _` | __/ _` | |/ / _ \\ '_ \\ | | |_| |/ / _ \\
 | |_| | (_| | || (_| |   <  __/ |_) || |  _|   <  __/
  \\___/ \\__,_|\\__\\__,_|_|\\_\\___|_.__(_)_|_| |_|\\_\\___|
                                                    
        1. Scan WiFi
        2. Attack WiFi (handshake, deauth, dll)
        3. Capture/Sniff Paket
        4. Analisa Paket (.pcap)
        5. Ganti Interface WiFi
        6. Keluar
        """)
        choice = input("Pilih menu [1-6]: ").strip()
        if choice == '1':
            scan_wifi(iface)
        elif choice == '2':
            attack_menu(iface)
        elif choice == '3':
            capture_packets(iface)
        elif choice == '4':
            analyze_packets()
        elif choice == '5':
            iface = select_interface()
        elif choice == '6':
            print("Keluar. Terima kasih!")
            break
        else:
            print("Menu tidak valid.")

if __name__ == "__main__":
    main_menu()
