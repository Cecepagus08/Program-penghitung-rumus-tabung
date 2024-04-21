import math
# ANSI escape codes for color formatting
GREEN = '\033[92m'
ORANGE = '\033[93m'
RED = '\033[91m'
END_COLOR = '\033[0m'

def hitung_luas_permukaan(r, t):
    if r % 7 == 0:
        luas_permukaan = 2 * 22 * r * (r + t) / 7
    else:
        luas_permukaan = 2 * 3.14 * r * (r + t)
    return luas_permukaan

def hitung_volume(r, t):
    if r % 7 == 0:
        volume = 22 * r**2 * t / 7
    else:
        volume = 3.14 * r**2 * t
    return volume

def hitung_luas_selimut(r, t):
    if r % 7 == 0:  # Cek apakah jari-jari adalah kelipatan dari 7
        luas_selimut = 2 * 22 * r * t / 7
    else:
        luas_selimut = 2 * 3.14 * r * t
    return luas_selimut

def hitung_tutup_tabung(r):
    if r % 7 == 0:   # Cek apakah nilai π adalah 22/7
        luas_tutup_tabung = r**2 * 22 / 7 # Menggunakan 22/7 sebagai nilai π
    else:
        luas_tutup_tabung = r**2 * 3.14  # Menggunakan 3.14 sebagai nilai π
    return luas_tutup_tabung

while True:
    print(f"{ORANGE}==================================={END_COLOR}")
    print("Penghitungan Luas dan Volume Tabung")
    print(f"{ORANGE}==================================={END_COLOR}")
    pilihan = int(input(f"Pilih operasi yang ingin dilakukan:\n1. Hitung Luas Permukaan Tabung\n2. Hitung Volume Tabung\n3. Hitung Luas Selimut Tabung\n4. Hitung Luas Tutup Tabung\n{RED}5. Keluar{END_COLOR}\nPilihan Anda (1/2/3/4/5): "))
    
    if pilihan == 5:
        print("Terima kasih!")
        break
    
    radius = float(input("Masukkan jari-jari tabung: "))

    if radius % 7 == 0:  # Cek apakah jari-jari adalah kelipatan dari 7
        pi_value = "22/7"
    else:
        pi_value = "3.14"

    if pilihan == 1:
        tinggi = float(input("Masukkan tinggi tabung: "))
        luas_permukaan = hitung_luas_permukaan(radius, tinggi)
        print(f"\n{GREEN}Diketahui{END_COLOR}\njari-jari: {radius}\ntinggi: {tinggi}\nπ: {pi_value}")
        print(f"hitung_luas_permukaan tabung = 2 × {pi_value} × {radius} ({radius} × {tinggi})")

        
        print(f"{ORANGE}Luas permukaan tabung: {luas_permukaan:.2f}{END_COLOR}\n")
    elif pilihan == 2:
        tinggi = float(input("Masukkan tinggi tabung: "))
        volume = hitung_volume(radius, tinggi)
        print(f"\n{GREEN}Diketahui{END_COLOR}\njari-jari: {radius}\ntinggi: {tinggi}\nπ: {pi_value}")
        print(f"hitung Volume tabung = {pi_value} × {radius}² × {tinggi}")
        
        print(f"{ORANGE}Volume tabung: {volume:.2f}{END_COLOR}\n")
    elif pilihan == 3:
        tinggi = float(input("Masukkan tinggi tabung: "))
        luas_selimut = hitung_luas_selimut(radius, tinggi)
        print(f"\n{GREEN}Diketahui{END_COLOR}\njari-jari: {radius}\ntinggi: {tinggi}\nπ: {pi_value}")
        print(f"hitung_luas_selimut = 2 × {pi_value} × {radius} × {tinggi}")
       
        
        print(f"{ORANGE}Luas selimut tabung: {luas_selimut:.2f}{END_COLOR}\n")
    elif pilihan == 4:
        luas_tutup_tabung = hitung_tutup_tabung(radius)
        print(f"\n{GREEN}Diketahui{END_COLOR}\njari-jari: {radius}\nπ: {pi_value}")
        
        print(f"hitung_tutup_tabung = {radius}² × {pi_value}")
       
        print(f"{ORANGE}Luas tutup tabung: {luas_tutup_tabung:.2f}{END_COLOR}\n")
    else:
        print("Pilihan tidak valid.")
