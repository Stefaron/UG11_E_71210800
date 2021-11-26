def hurufTengah(kata):
  if len(kata) < 5:
    return kata[(len(kata)-1)//2:(len(kata)+2)//2]
  elif len(kata) > 7:
    return kata[(len(kata)-3)//2:(len(kata)+4)//2]
  elif len(kata)%2 != 0:
    return kata[(len(kata)-2)//2:(len(kata)+3)//2]
  elif len(kata)%2 == 0:
    return kata[(len(kata)-2)//2:(len(kata)+3)//2]  


kata = str(input("Masukkan kata :"))
print("Huruf Tengah pada kata", kata, "adalah", hurufTengah(kata))