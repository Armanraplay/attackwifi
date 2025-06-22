import sys
from wifi_scan import scan_wifi
from wifi_attack import attack_menu
from packet_capture import capture_packets
from packet_analyze import analyze_packets

def main_menu():
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
        5. Keluar
        """)
        choice = input("Pilih menu [1-5]: ").strip()
        if choice == '1':
            scan_wifi()
        elif choice == '2':
            attack_menu()
        elif choice == '3':
            capture_packets()
        elif choice == '4':
            analyze_packets()
        elif choice == '5':
            print("Keluar. Terima kasih!")
            sys.exit(0)
        else:
            print("Menu tidak valid.")

if __name__ == "__main__":
    main_menu()
