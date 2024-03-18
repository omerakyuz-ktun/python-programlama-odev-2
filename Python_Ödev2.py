def harf_kontrol(karakter):
  if ord(karakter) >= ord("a") and ord(karakter) <= ord("z"):
    print("1. Girdiğiniz karakter bir harftir.")
  elif ord(karakter) >= ord("A") and ord(karakter) <= ord("Z"):
    print("1. Girdiğiniz karakter bir harftir.")
  else:
    print("1. Girdiğiniz karakter bir harf değildir.")

def kucuk_harfe_cevir(harf):
  if harf.isupper():
    print(f"2. '{harf}' harfinin küçük hali '{chr(ord(harf) + 32)}'.")
  else:
    print(f"2. Girdiğiniz harf '{harf}' zaten bir küçük harftir.")

def frekans_hesap(metin):
  harf_dict = {} 

  varsayilan_metin = metin

  for harf in varsayilan_metin:
    if harf.isalpha():  
      if harf in harf_dict:
        harf_dict[harf] += 1  
      else:
        harf_dict[harf] = 1  

  harf_sayisi = len(varsayilan_metin) 

  print(f"3. Frekans hesabı:")  
  for harf in harf_dict:
    using_rate = (harf_dict[harf] / harf_sayisi) * 100
    print(f"'{harf}': Kullanım Miktarı = {harf_dict[harf]} | Kullanım Oranı = {using_rate:.2f}%")
  print("----------------------------------------------------------------")

def imza():
  print("211220064\nÖmer İnanç AKYÜZ\n\033[1m\"Umutsuz durumlar yoktur. Umutsuz insanlar vardır. Ben hiçbir zaman umudumu yitirmedim.\" -Mustafa Kemal Atatürk\033[0m")

karakter = input("1. Kontrol edilecek karakteri girin: ")
harf = input("2. Küçük harfe çevrilecek harfi girin: ")
metin = input("3. Harf frekansı hesaplanacak metni girin: ")
print("----------------------------------------------------------------")
harf_kontrol(karakter)
kucuk_harfe_cevir(harf)
frekans_hesap(metin)
imza()