sıraları = [1,2,3,4,5,6,7]
takimlar = ["Galatasaray" , "Fenerbahçe","Beşiktaş","Trabzonspor","Newcastle United","Bayern München", "Real Madrid"]
puanlar = [78,75,73,66,65,63,51]
averajlar = [+1,+3,+5,+7,-1,0,-4]


for sira,takim, puan, averaj in zip (sıraları,takimlar,puanlar,averajlar):
    print(sira ,"-", takim, "-- Puan:", puan, "-- Averaj:",averaj)