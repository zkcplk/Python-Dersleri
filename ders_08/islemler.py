def islem_sec():
    print("\n*** İşlemler ***")
    print("1) Toplama")
    print("2) Çıkarma")
    print("3) Çarpma")
    print("4) Bölme")
    print("0) Çıkış")
    print("****************")
    
    return int(input("Lütfen bir işlem seçiniz: "))
   
def toplama():
    girilen_veri = input("Lütfen toplanacak sayıları, aralarında virgül olacak şekilde giriniz: ").strip().replace(" ", "")
    sayılar = girilen_veri.split(",")

    toplam = 0
    for i in sayılar:
        if i.isnumeric():
            toplam += int(i)
    
    print(f"Girilen sayıların toplamı: {toplam}")
    
def carpma():
    girilen_veri = input("Lütfen çarpılacak sayıları, aralarında virgül olacak şekilde giriniz: ").strip().replace(" ", "")
    sayılar = girilen_veri.split(",")

    carpim = 1
    for i in sayılar:
        if i.isnumeric():
            carpim *= int(i)
    
    print(f"Girilen sayıların çarpımı: {carpim}")
    
while True:
    islem = islem_sec()
    print("")
    
    if islem == 0:
        print("Program sonlandırıldı!")
        break
        
    elif islem == 1: 
        toplama()
    elif islem == 2: 
        s1 = int(input("Birinci sayı:"))
        s2 = int(input("İkinci sayı:"))
        print(f"Girilen sayıların farkı: {s1-s2}")
    elif islem == 3: 
        carpma()
    elif islem == 4:
        s1 = int(input("Birinci sayı:"))
        s2 = int(input("İkinci sayı:")) 
        print(f"Girilen sayıların bölümü: {s1 / s2}")
    else: print("Menüde olmayan bir işlem seçtiniz! Lütfen yeniden seçim yapın.")