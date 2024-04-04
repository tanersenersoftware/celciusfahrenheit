"""liste = [1,2,3,4,5,6]

for rakam in liste:
    print(rakam)""" #^ LİSTE İÇİNDEKİLERİ TEKER TEKER YAZDIRDIK

"""isim = "ahmet" , "kod" , "blogu" , "letter"

for kelime in isim:
    print(kelime)""" #^ İSİM DEĞİŞKENİNDEKİLERİ BLOK HALİNDE YAZDIRDIK

"""for i in range (1,17,2):
    print(i)""" #^ İKİLİ ŞEKİLDE 1,17 RANGE ARASI YAZDIRDIK

"""sonuc = 2
for i in range(105):
    sonuc *= 2
print(sonuc)""" #^ 2'NİN KUVVETLERİNİ ALDIK

liste1 = [1,2,3]
liste2 = "a","b","c","d"

for rakam in liste1:
    for harf in liste2:
        print(rakam,harf)