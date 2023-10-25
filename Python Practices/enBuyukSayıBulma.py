#Kullanıcının girdiği üç sayı arasında en büyük olanı bulan ve sonucu yazdıran bir program yazınız

birinciSayi = float(input("Birinci sayiyi giriniz: "))
ikinciSayi = float(input("İkinci sayiyi giriniz: "))
ucuncuSayi = float(input("Üçüncü sayiyi giriniz: "))

enBuyukSayi = max(birinciSayi, ikinciSayi, ucuncuSayi)

print("En büyük sayi : ", enBuyukSayi)
        