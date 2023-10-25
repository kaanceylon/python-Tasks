#Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteriniz.

maas = float (input("İşçinin maaşını giriniz: "))
zam = float (input("Yapılan zam oranını (yüzde olarak) giriniz: "))

zamMiktarı = maas * (zam / 100)

yeniMaas = maas + zamMiktarı

print("Yeni maaşınız: ", yeniMaas)