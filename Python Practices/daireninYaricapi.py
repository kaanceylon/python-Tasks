#Soru-4: Dairenin alanını ve çevresini hesaplayan python kodunu yazınız. (dairenin yarıçapını kullanıcıdan alınız)

import math

yariCap = input("Dairenin yarıçapını giriniz: ") # kullanıcıdan yarıçap aldık

alan = math.pi * yariCap ** 2 # # Dairenin alanını hesaplamak için (π * r^2)
cevre = 2 * math.pi * yariCap # Dairenin çevresini hesaplamak için (2 * π * r)

print(f"Dairenin alanı: {alan}, çevresi: {cevre}")