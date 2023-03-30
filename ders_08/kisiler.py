import os
import json

def islem_sec():
    print("\n*** İşlemler ***")
    print("0) Çıkış")
    print("1) Ekle")
    print("2) Sil")
    print("3) Düzenle")
    print("4) Listele")
    print("****************")
    
    return int(input("Lütfen bir işlem seçiniz: "))

def çıkış():
    with open(dosya, "w") as file:
        json.dump(kisiler, file, indent=4) 
        
    print("Program sonlandırıldı!");
        

def sonraki_id():
    max_id = 0
    for i in kisiler:
        max_id = max(i.get("id"), max_id)
        
    return max_id+1
    
    
def ekle():
    id_ = sonraki_id()
    ad = input("Eklenecek kişinin Adı: ").capitalize()
    soyad = input("Eklenecek kişinin Soyadı: ").capitalize()
    tel = input("Eklenecek kişinin Telefonu: ")
    şehir = input("Eklenecek kişinin Şehri: ").capitalize()
    
    kisiler.append({"id":id_, "Ad":ad, "Soyad":soyad, "Telefon":tel, "Şehir":şehir})
    listele()
    
def listele():
    print("")
    print("---------- Kişiler Listesi ----------")
    
    if len(kisiler) < 1:
        print("Listede kimse yok!")
    else:   
        for i in kisiler:
            for k,v in i.items():
                print(v, end=", ")
            
            print("")
    print("")
    
def sil():
    toplam = len(kisiler)
    
    if toplam < 1:
        print("Listede silinecek kimse yok!")
    else: 
        id_ = int(input("Silinecek kişinin id'sini giriniz: "))
        for i in range(toplam):
            if kisiler[i].get("id") == id_:
                kisiler.pop(i)
                break # sileceğimizi sildikten sonra, diğerlerini dolaşmaya gerek yok!
        
        listele()
        
def duzenle():
    toplam = len(kisiler)
    
    if toplam < 1:
        print("Listede silinecek kimse yok!")
    else: 
        id_ = int(input("Düzenlenecek kişinin id'sini giriniz: "))
        for i in range(toplam):
            if kisiler[i].get("id") == id_:
                kisiler.pop(i)
                break
        
        ad = input("Eklenecek kişinin Adı: ").capitalize()
        soyad = input("Eklenecek kişinin Soyadı: ").capitalize()
        tel = input("Eklenecek kişinin Telefonu: ")
        şehir = input("Eklenecek kişinin Şehri: ").capitalize()

        kisiler.append({"id":id_, "Ad":ad, "Soyad":soyad, "Telefon":tel, "Şehir":şehir})
        listele()

kisiler = []
dosya = "kisiler.json"

# eğer dosya varsa, json modülü ile load ediyoruz.
if os.path.exists(dosya):
    with open(dosya, "r", encoding="UTF-8") as file:
        kisiler = json.load(file)
        
# eğer dosya yoksa, boş olarak oluşturuyoruz.
else: 
    with open(dosya, "w", encoding="UTF-8") as file:
        pass
        
while True:
    islem = islem_sec()
    print("")
    
    if islem == 0: çıkış(); break
    elif islem == 1: ekle()
    elif islem == 2: sil()
    elif islem == 3: duzenle()
    elif islem == 4: listele()
    else: print("Menüde olmayan bir işlem seçtiniz! Lütfen yeniden seçim yapın.")
