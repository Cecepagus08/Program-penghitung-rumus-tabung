
import math

# ANSI escape codes for color formatting
GREEN = '\033[92m'
ORANGE = '\033[93m'
RED = '\033[91m'
END_COLOR = '\033[0m'


def format_number(num):
    if isinstance(num, float) and num.is_integer():
        return int(num)
    return num


while True:
    print(f"{ORANGE}==================================={END_COLOR}")
    print("Penghitungan Luas dan Volume Tabung")
    print(f"{ORANGE}==================================={END_COLOR}")
    pilihan = int(input(f"Pilih operasi yang ingin dilakukan:\n1. Hitung Luas Permukaan Tabung\n2. Hitung Volume Tabung\n3. Hitung Luas Selimut Tabung\n4. Hitung Luas Tutup Tabung\n{RED}5. Keluar{END_COLOR}\nPilihan Anda (1/2/3/4/5): "))
    
    if pilihan == 5:
        print("Terima kasih!")
        break
    
    radius = float(input("Masukkan jari-jari tabung: "))
    jari_jari = format_number(radius)
    
    if radius % 7 == 0:
      pi_value = "22/7"
    else:
      pi_value = "3.14"
    
    if pilihan == 1:
      # LUAS PERMUKAAN TABUNG
      # l = 2πr(r+t)
        tinggi =float(input("Masukkan tinggi tabung: ")) 
        tinggi_tabung = format_number(tinggi)
        print(f"  rumus permukaan tabung {RED}2πr(r+t){END_COLOR}")
        print(f"  {ORANGE}Diketahui{END_COLOR}")
        print(f"  jari-jari: {jari_jari}")
        print(f"  tinggi: {tinggi_tabung}")
        print(f"  π: {pi_value}")
        if radius % 7 == 0:
            step1 = radius + tinggi_tabung
            step2 = radius / 7
            step3 = 2 * 22
            step4 = step3 * step2
            step5 = step4 * step1
            
            print(f"  2 x 22/7 × {jari_jari} × ( {jari_jari} + {tinggi_tabung} ) ")
            print(f"  2 × 22/7 × {jari_jari} × {format_number(step1)}")
            print(f"  2 × 22 × {format_number(step2)} × {format_number(step1)}")
            print(f"  {format_number(step3)} × {format_number(step2)} × {format_number(step1)}")
            print(f"  {format_number(step4)} × {format_number(step1)}")
            print(f"  Luas permukaan tabung: {step5}\n")
        else:
            step1 = radius + tinggi
            step2 = 2 * 3.14
            step3 = step2 * radius
            step4 = step3 * step1
            

            print(f"  2 x 3.14 × {jari_jari} × ( {jari_jari} + {tinggi_tabung} )")
            print(f"  2 × 3.14 × {jari_jari} × {format_number(step1)}")
            print(f"  {format_number(step2)} × {jari_jari} × {format_number(step1)}")
            print(f"  {format_number(step3)} × {format_number(step1)}")
            print(f"  Luas permukaan tabung: {format_number(step4)}\n")
    elif pilihan == 2:
      # hitung volume tabung
      # v = πr²t
      tinggi =float(input("Masukkan tinggi tabung: "))   
      tinggi_tabung = format_number(tinggi)
      print(f"  rumus volume tabung {RED}2πr²t{END_COLOR}")
      print(f"  {ORANGE}Diketahui{END_COLOR}")
      print(f"  jari-jari: {jari_jari}")
      print(f"  tinggi: {tinggi_tabung}")
      print(f"  π: {pi_value}")
      if radius % 7 == 0:
        pangkat = radius**2
        step1 = radius**2 / 7
        step2 = step1 * 22
        step3 = step2 * tinggi
        print(f"  22/7 × {jari_jari}² × {tinggi_tabung}")
        print(f"  22/7 × {format_number(pangkat)} × {tinggi_tabung}")
        print(f"  22 × {format_number(step1)} × {tinggi_tabung}")
        print(f"  {format_number(step2)} × {tinggi_tabung}")
        print(f"  volume tabungnya adalah: {format_number(step3)}\n")
      else:
          pangkat = radius**2
          step1 = 3.14 * pangkat
          step2 = step1 * tinggi
          print(f"  3,14 × {jari_jari}² × {tinggi_tabung}")
          print(f"  3,14 × {format_number(pangkat)} × {tinggi_tabung}")
          print(f"  {format_number(step1)} × {tinggi_tabung}")
          print(f"  volume tabungnya adalah :  {format_number(step2)}\n")
    elif pilihan == 3:
      # hitung luas Selimut
      #  l = 2πrt
      tinggi =float(input("Masukkan tinggi tabung: "))  
      tinggi_tabung = format_number(tinggi)
      print(f"  rumus luas Selimut tabung {RED}2πrt{END_COLOR}")
      print(f"  {ORANGE}Diketahui{END_COLOR}")
      print(f"  jari-jari: {jari_jari}")
      print(f"  tinggi: {tinggi_tabung}")
      print(f"  π: {pi_value}")
      if radius % 7 == 0:
          step1 = radius / 7
          step2 = 2 * 22 
          step3 = step2 * step1
          step4 = step3 * tinggi
          
          print(f"  2 × 22/7 {jari_jari} × {tinggi_tabung}")
          print(f"  2 × 22 × {format_number(step1)} × {tinggi_tabung}")
          print(f"  {format_number(step2)} × {format_number(step1)} × {tinggi_tabung}")
          print(f"  {format_number(step3)} × {tinggi_tabung}")
          print(f"  luas Selimut tabung adalah: {format_number(step4)}\n")
      else:
          step1 = 2 * 3.14
          step2 = step1 * radius 
          step4 = step2 * tinggi
          print(f"  2 × 3.14 × {jari_jari} × {tinggi_tabung}")
          print(f"  {format_number(step1)} × {jari_jari} × {tinggi_tabung}")
          print(f"  {format_number(step2)} × {tinggi_tabung}")
          print(f"  luas Selimut tabung adalah: {format_number(step4)}\n")
    elif pilihan == 4:
      # luas tutup tabung
      # l = π r²
        print(f"  rumus tutup tabung {RED}πr²{END_COLOR}")
        print(f"  {ORANGE}Diketahui{END_COLOR}")
        print(f"  jari-jari: {jari_jari}")
        print(f"  π: {pi_value}")
        if radius % 7 == 0:
          pangkat = radius**2
          step1 = pangkat / 7
          step2 = 22 * step1
          
          print(f"  22/7 × {jari_jari}²")
          print(f"  22/7 {format_number(pangkat)}")
          print(f"  22 × {format_number(step1)}")
          print(f"  luas tutup tabung nya adalah: {format_number(step2)}\n")
        else:
          pangkat = radius**2
          step1 = 3.14 * pangkat
          print(f"  3.14 × {jari_jari}²")
          print(f"  3.14 × {format_number(pangkat)}")
          print(f"  luas tutup tabungnya adalah: {format_number(step1)}\n")
          

    else:
        print("Pilihan tidak valid.")
