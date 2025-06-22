def attack_menu():
    print("[*] Menu attack (fitur dasar)")
    print("1. Capture handshake WPA/WPA2")
    print("2. Serangan deauth")
    print("3. Kembali ke menu utama")
    choice = input("Pilih aksi: ").strip()
    if choice == '1':
        print("Fitur capture handshake akan dikembangkan...")
        # Tambahkan implementasi handshake capture di sini
    elif choice == '2':
        print("Fitur deauth akan dikembangkan...")
        # Tambahkan implementasi deauth di sini
    else:
        print("Kembali ke menu utama.")