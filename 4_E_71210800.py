import random

def generate(level):
    operasi = ['+','-','/','*']
    operator = random.choice(operasi)
    if level == '1':
        angka1 = random.randint(20,50)
        angka2 = random.randint(20,50)
        operator = random.choice(operasi)
        hasil = eval( str(angka1) + operator + str(angka2))
        hasil = round(hasil,3)
        print("Berapakah hasil dari ", angka1,operator,angka2)
        jawab = float(input("Masukkan jawaban anda : "))
        if jawab == hasil:
            return print("Jawaban anda benar!")
        else :
            print("Jawaban anda salah !")
            print("Hasil dari ", angka1,operator,angka2, "=", hasil)

    elif level == "2":
        angka1 = random.randint(20,70)
        angka2 = random.randint(20,70)
        angka3 = random.randint(20,70)
        operator1 = random.choice(operasi)
        operator2 = random.choice(operasi)
        hasil = eval( str(angka1) + operator1 + str(angka2) + operator2 + str(angka3))
        hasil = round(hasil,3)
        print("Berapakah hasil dari ",angka1,operator1,angka2,operator2,angka3)
        jawab = float(input("Masukkan jawaban anda : "))
        if jawab == hasil:
            return print("Jawaban anda benar!")
        else :
            print("Jawaban anda salah !")
            print("Hasil dari ", angka1,operator1,angka2,operator2,angka3, "=", hasil)

    elif level == "3":
        angka1 = random.randint(20,100)
        angka2 = random.randint(20,100)
        angka3 = random.randint(20,100)
        angka4 = random.randint(20,100)
        operator1 = random.choice(operasi)
        operator2 = random.choice(operasi)
        operator3 = random.choice(operasi)
        hasil = eval( str(angka1) + operator1 + str(angka2) + operator2 + str(angka3) + operator3 + str(angka4))
        hasil = round(hasil,3)
        print("Berapakah hasil dari ",angka1,operator1,angka2,operator2,angka3,operator3,angka4)
        jawab = float(input("Masukkan jawaban anda : "))
        if jawab == hasil:
            return print("Jawaban anda benar!")
        else :
            print("Jawaban anda salah !")
            print("Hasil dari ", angka1,operator1,angka2,operator2,angka3,operator3,angka4, "=", hasil)




print("""====Program aritmatik Dasar====
Pilihan level yang tersedia :
1. Easy
2. Medium
3. Hard""")

level = str(input("Masukkan tingkatan yang ingin anda coba : "))
generate(level)