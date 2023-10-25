#1-Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini (VKİ = ağırlık/(boy*boy)) hesaplayınız.
# (VKİ = ağırlık/(boy*boy)) 

boy = float (input ("Lütfen boyununuzu giriniz: "))
kilo = float (input ("Lütfen kilonuzu giriniz: "))

VKI = kilo / (boy * boy)
print("Vücut kitle indeksiniz: ", VKI)


