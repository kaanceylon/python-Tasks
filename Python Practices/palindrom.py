# Kullanıcıdan alınan bir sayının palindrom olup olmadığını bulan bir program yazınız.

sayi = input ("Lütfen bir sayi giriniz: ")

palSayi = sayi[::-1] # Sayının ters haline bakalım

if sayi == palSayi:
    print("Girdiğiniz sayi bir palindrom sayidir")
else :
    print("Girdiğiniz sayi palindrom sayisi değildir.")