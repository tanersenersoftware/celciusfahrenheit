
sinav_sonucu = float(input("Lütfen sınav sonucunu girip, harf karşılığını öğrenin: "))
if 0 <= sinav_sonucu <= 100:
    if sinav_sonucu >= 88:
        print("Dersi AA ile geçtiniz. Tebrikler!")
    elif sinav_sonucu >=81:
        print("Dersi BA ile geçtiniz. Tebrikler!")
    elif sinav_sonucu >=74:
        print("Dersi BB ile geçtiniz. Tebrikler!")
    elif sinav_sonucu >=67:
        print("Dersi CB ile geçtiniz. Tebrikler!")
    elif sinav_sonucu >=60:
        print("Dersi CC ile geçtiniz. Tebrikler!")
    else:
        print("Dersi başarıyla tamamlayamadınız. Lütfen bu dersi tekrar seçiniz.")
else:
    print("Lütfen geçerli bir not puanı giriniz.")