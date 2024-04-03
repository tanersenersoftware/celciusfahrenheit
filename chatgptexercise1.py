print("Sıcaklık derecesi dönüştürme aracına hoşgeldiniz.")
name = input("Lütfen isminizi girer misiniz: ")
if name == "":
    print("İsminizi söylemediniz.")
else:
    print(f"Merhaba {name}, İsmini girdiğin için teşekkür ederim.")

fahrenheit = 33.8
sicaklik = float(input("Lütfen hava durumunun kaç Celcius olduğunu söyleyin ve onu Fahrenheit'a dönüştürelim.:"))
if sicaklik <= 100:
    print(str("Hava durumu şuan"), sicaklik + fahrenheit , str("fahrenheit olarak hesaplanmıştır."))