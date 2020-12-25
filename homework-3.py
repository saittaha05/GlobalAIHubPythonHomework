import random

name = input("isminizi giriniz : ")
print("welcome ",name)

kelimeler = ["at" , "silah" , "lise" , "alkış" , "kedi" , "bilgisayar" , "klavye" , "mause" , "portakal" , "el"]
kelime = random.choice(kelimeler)
tahminSayisi = 5
harfler = []
x = len(kelime)
z = list('_' * x)
print(' '.join(z), end='\n')
while tahminSayisi > 0:
    y = input("Bir harf tahmin edin : ")
    if y in harfler:
        print("Lutfen daha once tahmin ettiginiz harfleri tekrar tahmin etmeyin...")
        continue

    elif len(y) > 1:
        print("Lutfen sadece bir harf girin :")
        continue

    elif y not in kelime:   
        tahminSayisi -= 1
        print("yanlis tahmin!. {} tane tahmin hakkiniz kaldi.".format(tahminSayisi))

    else:
        for i in range(len(kelime)):
            if y == kelime[i]:
                print("Dogru Tahmin")
                z[i] = y
                harfler.append(y)
        print(' '.join(z), end='\n')

    cevap = input("Kelimenin tamamini tahmin etmek istiyor musunuz? ['e' veya 'h'] : ")

    if cevap == "e":
        tahmin = input("Kelimenin tamamini tahmin edebilirsiniz : ")
        if tahmin == kelime:
            print("Tebrikler bildiniz...")
            break
        else:
            tahminSayisi -= 1
            print("Yanlis tahmin ettiniz. {} tane tahmin hakkiniz kaldi.".format(tahminSayisi))


    if tahminSayisi == 0:
        print("Tahmin hakkiniz kalmadi. Kaybettiniz! Adam Asildi.")
        break 
