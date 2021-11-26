def pangkatAngka():
    print("Masukkan angka yang ingin dipangkatkan")
    angka = float(input(":"))
    print("Ingin memodifikasi pangkat? (yes/no)")
    pilih = str(input(":"))
    if pilih == "yes":
        pangkat = int(input("Masukkan nilai pangkat :"))
        print("Hasil dari ", angka,"^",pangkat, "=",angka**pangkat)
    else :
        print("Hasil dari ", angka,"^ 2 =",angka**2)

def pangkatAkar():
    print("Masukkan angka yang ingin diakarkan")
    angka = float(input(":"))
    print("Ingin memodifikasi akar? (yes/no)")
    pilih = str(input(":"))
    if pilih == "yes":
        akar = float(input("Masukkan nilai akar :"))
        hitung = angka**(1/(akar))
        print("Hasil akar pangkat", akar, "dari", angka, "adalah", (hitung))
    else :
        hitung = angka**(1/2)
        print("Hasil akar pangkat 2 dari", angka, "adalah", "{:.2f}".format(hitung))

print("""Menu Program yang tersedia
1. Pangkat angka
2. Akarkan bilangan
""")

menu = str(input("Masukkan pilihan yang diinginkan : "))
if menu == "1":
    pangkatAngka()
elif menu == "2":
    pangkatAkar()
else :
    print("-")