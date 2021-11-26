def hitungKata():
    kalimat = str(input("Masukkan sebuah kalimat/kata : "))
    cek = str(input("Masukkan kata yang ingin dihitung : "))
    y = str.lower(kalimat).count(cek)
    print("Terdapat", y, "kata", cek, "di dalam string")
    return y

def cekkata():
    kalimat = str(input("Masukkan sebuah kalimat/kata : "))
    cek = str(input("Masukkan kata yang ingin dicek : "))
    if cek in kalimat :
        print("Kata", cek, "terdapat di dalam string")
        print("String diubah menjadi :")
        ubah = cek.upper()
        hasil = kalimat.replace(cek,ubah)
        print(hasil)
    else :
        print("Kata", cek, "tidak terdapat dalam string")
        print("String diubah menjadi :")
        print(kalimat , cek)

def ubahKata():
    kalimat = str(input("Masukkan sebuah kalimat/kata : "))
    kata = str(input("Masukkan kata yang ingin diubah : "))
    ganti = str(input("Masukkan kata pengganti : "))
    print("Anda akan mengubah kata", kata, "menjadi", ganti, "sebanyak 1x")
    pilih = str(input("Apakah anda ingin mengubah total penggantian kata? (yes/no) : "))
    if pilih == "no" :
        print("String berhasil diubah menjadi :")
        print(kalimat.replace(kata,ganti,1))
    else :
        jumlahGanti = int(input("MAsukkan jumlah total penggantian : "))
        print("String berhasil diubah menjadi :")
        print(kalimat.replace(kata,ganti,jumlahGanti))





print("""====Program manupulasi string====
Pilihan Menu :
1. Hitung Kata
2. Cek kata
3. Ubah kata""")

menu = input("Pilihan anda :")
if menu == "1" :
    hitungKata()
elif menu == "2" :
    cekkata()
elif menu == "3":
    ubahKata()