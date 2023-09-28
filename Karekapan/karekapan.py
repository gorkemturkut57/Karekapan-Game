def degerbul(x): #Kulllanıcının girdiği sütun isimlerini listede aratmak için harfleri uygun indexlere dönüştüren fonksiyon.
    if str(x) == "A":
        DEGERI = 0
    elif str(x) == "B":
        DEGERI = 1
    elif str(x) == "C":
        DEGERI = 2
    elif str(x) == "D":
        DEGERI = 3
    elif str(x) == "E":
        DEGERI = 4
    elif str(x) == "F":
        DEGERI = 5
    elif str(x) == "G":
        DEGERI = 6
    else:
        DEGERI = 7
    return int(DEGERI)
def harfbul(x): #Indexleri uygun harflere dönüştüren fonksiyon.
    if x == 0:
        HARFI = "A"
    elif x == 1:
        HARFI = "B"
    elif x == 2:
        HARFI = "C"
    elif x == 3:
        HARFI = "D"
    elif x == 4:
        HARFI = "E"
    elif x == 5:
        HARFI = "F"
    elif x == 6:
        HARFI = "G"
    elif x == 7:
        HARFI = "H"
    return HARFI
def oyun_alani_olustur(): #Kullanıcıdan 3-7 arasında bir değer girene kadar istediği satır sayısını alan fonksiyon.
    DEVAM = "E"
    while DEVAM == "E":
        try:
            yatay_cizgi_sayisi = int(input("Oyun alanında kaç tane yatay çizgi bulunsun [3-7]:"))
            if 3 <= yatay_cizgi_sayisi <= 7: #Burada alınan input değerinin 3-7 arasında olup olmadığı kontrol ediliyor.
                DEVAM = "H"
            else:
                print("Lütfen geçerli bir değer giriniz!") #3-7 arasında değer girilmezse fonksiyon buraya giriyor.
        except ValueError:
            print("Lütfen geçerli bir değer giriniz!") #Sayı girilmezse fonksiyon buraya giriyor.
    return yatay_cizgi_sayisi
def oyun_alani_ciz(satir, sutun): #Kullanıcıdan alınan satır sayısına göre oyun tablosunu boş olarak çizen fonksiyon.
    SUTUN_ISIMLERI = ["A", "B", "C", "D", "E", "F", "G", "H"] #Bu liste sütun isimlerinin alabileceği harfleri gösteriyor.
    SAYAC = 0
    for isim in SUTUN_ISIMLERI: #Burada kullanıcıdan alınan satır değerine göre sütun isimleri tablonun başına yazdırılıyor.
        SAYAC += 1
        if SAYAC < sutun: #Son satıra gelene kadar 3 boşluk bırakarak harfler yazdırılıyor.
            print(isim, end="   ")
        else:
            print(isim) #Son satırda harf yazdırma işlemi bitiriliyor.
            break
    SATIRLAR = []
    for satirlar in range(satir):
        SUTUNLAR = []
        for sutunlar in range(sutun):
            SUTUNLAR.append("*") #Taş yerleştirilecek yerlere * işareti koyuluyor.
        SATIRLAR.append(SUTUNLAR) #Burda liste içinde liste kullanarak tabloyu matris şeklinde oluşturuyoruz.Satırlar içindeki listelerin her biri satır,bu listelerdeki elemanlar da sütunların her birine gelen taşları temsil ediyor.
    say1 = 0
    for i in SATIRLAR:
        say1 = say1 + 1
        say = 0
        for j in i:
            say += 1
            if say < sutun:
                print(j, end="---")
            else:
                print(j, say1)
                if say1 <= satirlar:
                    print("|   " * sutun)
    return SATIRLAR
def oyun_alani_devamini_ciz(LISTE): #Oyunun ilerleyen kısımlarında kullanıcıdan alınan değerlere göre tablo tekrar tekrar yazdırılıyor.
    SUTUN_ISIMLERI = ["A", "B", "C", "D", "E", "F", "G", "H"]
    SAYAC = 0
    for i in SUTUN_ISIMLERI:
        SAYAC += 1
        if SAYAC == SUTUN_SAYISI:
            print(i)
            break
        else:
            print(i, end="   ")
    sayac = 0
    for j in LISTE:
        SAY = 0
        sayac += 1
        for k in j:
            SAY += 1
            if SAY == SUTUN_SAYISI:
                print(k, sayac)
            else:
                print(k, end="---")
        if sayac < SATIR_SAYISI:
            print("|   " * SUTUN_SAYISI)
SATIR_SAYISI = oyun_alani_olustur()
SUTUN_SAYISI = SATIR_SAYISI + 1
OYUN_LISTESI = oyun_alani_ciz(SATIR_SAYISI, SUTUN_SAYISI)
def tas_yerlestir(LISTE): #Kullanıcıdan uygun yerlere taş koymasını isteyen fonksiyon.
    SUTUN_ISIMLERI = ["A", "B", "C", "D", "E", "F", "G", "H"]
    TASIN_KONULABILECEGI_HARFLER = []
    TASIN_KONULABILECEGI_SAYILAR = []
    SAY = 0
    BEYAZLARIN_KONUMLARI = []
    SIYAHLARIN_KONUMLARI = []
    for harf in SUTUN_ISIMLERI: #Burada kullanıcının girdiği komutun ilk indexinin doğru harf olup olmadığı kontrol ediliyor.
        SAY += 1
        if SAY == SUTUN_SAYISI:
            TASIN_KONULABILECEGI_HARFLER.append(harf)
            break #Son sütuna gelince harf ekleme durduruluyor.
        else:
            TASIN_KONULABILECEGI_HARFLER.append(harf)
    for sayi in range(1, SATIR_SAYISI + 1):
        TASIN_KONULABILECEGI_SAYILAR.append(str(sayi)) #Kullanıcıdan alınan komutun ikinci indexinin doğru olup olmadığını kontrol etmek için yapılıyor.
    TOPLAM_HAMLE_SAY = SUTUN_SAYISI * SATIR_SAYISI
    for i in range(TOPLAM_HAMLE_SAY): #Beyaz taş-Siyah taş kontrolü yapılıyor.
        DEVAM = "E"
        if i % 2 == 0:
            HAMLE = "B"
        else:
            HAMLE = "S"
        while DEVAM == "E":
            try:
                tasin_konumu = input("Taşı koymak istediğiniz konumu giriniz:")
                tasin_konumu = tasin_konumu.upper()
                if tasin_konumu[0] in TASIN_KONULABILECEGI_HARFLER and tasin_konumu[
                    1] in TASIN_KONULABILECEGI_SAYILAR and len(
                    tasin_konumu) == 2 and tasin_konumu not in BEYAZLARIN_KONUMLARI and tasin_konumu not in SIYAHLARIN_KONUMLARI:
                    DEVAM = "H"
                else:
                    print("Lütfen geçerli bir değer giriniz!")
            except IndexError:
                print("Lütfen geçerli bir değer giriniz!")
        SATIR_NO = tasin_konumu[1]
        SUTUN_NO = 0
        for k in SUTUN_ISIMLERI:
            SUTUN_NO += 1
            if k == tasin_konumu[0]:
                break
        if HAMLE == "B":
            BEYAZLARIN_KONUMLARI.append(tasin_konumu) #Beyazları koyduğumuz yerlerin ismini tuttuğumuz liste.
            OYUN_LISTESI[int(SATIR_NO) - 1][int(SUTUN_NO) - 1] = "B"
        else:
            SIYAHLARIN_KONUMLARI.append(tasin_konumu) #Siyahları koyduğumuz yerlerin ismini tuttuğumuz liste.
            OYUN_LISTESI[int(SATIR_NO) - 1][int(SUTUN_NO) - 1] = "S"
        oyun_alani_devamini_ciz(OYUN_LISTESI) #Taş yerleştirme işlemi bittikten sonra tekrar oyun tablosu çizdiriyoruz.
    return BEYAZLARIN_KONUMLARI, SIYAHLARIN_KONUMLARI
beyazlarin_konumlari, siyahlarin_konumlari = tas_yerlestir(OYUN_LISTESI)
def kare_bul(liste): #Kare sayısını bulmak için yapılmış fonksiyon.
    BEYAZ_KARELERIN_BULUNDUGU_KONUMLAR = [] #Beyaz kareleri oluşturan taşların indexlerinin bulunduğu liste
    SIYAH_KARELERIN_BULUNDUGU_KONUMLAR = [] #Siyah kareleri oluşturan taşların indexlerinin bulunduğu liste
    KARE_SAYILARI = {"beyaz kareler": 0, "siyah kareler": 0} #Kare sayılarının bulunduğu sözlük.
    for i in range(0, int(SATIR_SAYISI)):
        for j in range(0, int(SUTUN_SAYISI)):
            try:
                if liste[i][j] == liste[i][j + 1] == liste[i + 1][j] == liste[i + 1][j + 1]: #Kare oluşturup oluşturmadığını kontrol ettiğimiz yer.
                    if liste[i][j] == "B":
                        GUNCEL_KARE_SAYISI = 1 + KARE_SAYILARI.get("beyaz kareler")
                        KARE_SAYILARI.update({"beyaz kareler": GUNCEL_KARE_SAYISI})
                        BEYAZ_KARELERIN_BULUNDUGU_KONUMLAR.append([i, j])
                        BEYAZ_KARELERIN_BULUNDUGU_KONUMLAR.append([i, j + 1])
                        BEYAZ_KARELERIN_BULUNDUGU_KONUMLAR.append([i + 1, j])
                        BEYAZ_KARELERIN_BULUNDUGU_KONUMLAR.append([i + 1, j + 1])
                    else:
                        GUNCEL_KARE_SAYISI = 1 + KARE_SAYILARI.get("siyah kareler")
                        KARE_SAYILARI.update({"siyah kareler": GUNCEL_KARE_SAYISI})
                        SIYAH_KARELERIN_BULUNDUGU_KONUMLAR.append([i, j])
                        SIYAH_KARELERIN_BULUNDUGU_KONUMLAR.append([i, j + 1])
                        SIYAH_KARELERIN_BULUNDUGU_KONUMLAR.append([i + 1, j])
                        SIYAH_KARELERIN_BULUNDUGU_KONUMLAR.append([i + 1, j + 1])
            except:
                print("", end="")
    for i in BEYAZ_KARELERIN_BULUNDUGU_KONUMLAR:
        a = BEYAZ_KARELERIN_BULUNDUGU_KONUMLAR.count(i) #Birden fazla kare oluşturan taşlar birden fazlka kez yazıldığı için onları çıkarıyoruz.
        if a > 1:
            for b in range(a - 1):
                BEYAZ_KARELERIN_BULUNDUGU_KONUMLAR.remove(i)
    for i in SIYAH_KARELERIN_BULUNDUGU_KONUMLAR:
        a = SIYAH_KARELERIN_BULUNDUGU_KONUMLAR.count(i)
        if a > 1:
            for b in range(a - 1):
                SIYAH_KARELERIN_BULUNDUGU_KONUMLAR.remove(i) #Birden fazla kare oluşturan taşlar birden fazlka kez yazıldığı için onları çıkarıyoruz.
    return KARE_SAYILARI["beyaz kareler"], KARE_SAYILARI[
        "siyah kareler"], BEYAZ_KARELERIN_BULUNDUGU_KONUMLAR, SIYAH_KARELERIN_BULUNDUGU_KONUMLAR
BEYAZ_KARE_SAYISI, SIYAH_KARE_SAYISI, BEYAZ_KARELERI_OLUSTURAN_TASLARIN_KONUMLARI, SIYAH_KARELERI_OLUSTURAN_TASLARIN_KONUMLARI = kare_bul(
    OYUN_LISTESI)
def tas_sil(beyaz_kare_sayilari, siyah_kare_sayilari,LISTE_BEYAZ,LISTE_SIYAH): #Kullanıcı kare oluşturduğunda karşıdan taş silmesi için çağırdığımız fonksiyon.
    beyazlarin_gidebilecegi_yerler = []
    siyahlarin_gidebilecegi_yerler = []
    beyazlarin_alabilecegi_taslar = []
    siyahlarin_alabilecegi_taslar = []
    SUTUN_ISIMLERI = ["A", "B", "C", "D", "E", "F", "G", "H"]
    say = 0
    GIDILEBILECEK_VE_ALINABILECEK_YER = []
    for i in SUTUN_ISIMLERI:
        say += 1
        if say > SUTUN_SAYISI:
            break
        for j in range(1, SATIR_SAYISI + 1): #İlk önce tüm ihtimalleri listelere ekliyoruz.
            GIDILEBILECEK_VE_ALINABILECEK_YER.append(i + str(j))
            beyazlarin_gidebilecegi_yerler.append(i + str(j))
            siyahlarin_gidebilecegi_yerler.append(i + str(j))
            beyazlarin_alabilecegi_taslar.append(i + str(j))
            siyahlarin_alabilecegi_taslar.append(i + str(j))
    SATIR_INDEX=-1
    for i in OYUN_LISTESI:
        SUTUN_INDEX=-1
        SATIR_INDEX+=1
        for j in i:
            SUTUN_INDEX+=1
            if j=="*":
                    beyazlarin_alabilecegi_taslar.remove(harfbul(SUTUN_INDEX)+str(SATIR_INDEX+1))
                    siyahlarin_alabilecegi_taslar.remove(harfbul(SUTUN_INDEX)+str(SATIR_INDEX+1))

    for i in beyazlarin_konumlari: #Daha sonra olamayacak ihtimalleri listelerden çıkarıyoruz.
        beyazlarin_alabilecegi_taslar.remove(i)
    for a in siyahlarin_konumlari:
        siyahlarin_alabilecegi_taslar.remove(a)
    for i in (LISTE_BEYAZ):
        YAZILACAK_DEGER=harfbul(i[1])+str(i[0]+1)
        try:
            siyahlarin_alabilecegi_taslar.remove(YAZILACAK_DEGER)
        except:
            print("", end="")
    for a in (LISTE_SIYAH):
        YAZILACAK_DEGER=harfbul(a[1])+str(a[0]+1)
        try:
            beyazlarin_alabilecegi_taslar.remove(YAZILACAK_DEGER)
        except:
            print("", end="")
    if beyaz_kare_sayilari == siyah_kare_sayilari == 0: #İki rengin de başta karesi yoksa beyazlara 1 taş alma hakkı veriyoruz.
        beyaz_kare_sayilari = 1
    for i in range(1, beyaz_kare_sayilari + 1):
        devam = "e"
        while devam == "e":
            almak_istenilen_tas = input("Almak istediğiniz siyah taşın konumunu giriniz:") #Taş almak için kullanıcıdan girdi isteniyor ve geçerli değer girilene kadar tekrar tekrar soruluyor.
            almak_istenilen_tas = almak_istenilen_tas.upper()
            if almak_istenilen_tas in beyazlarin_alabilecegi_taslar:
                devam = "H"
                index=degerbul(almak_istenilen_tas[0])
                OYUN_LISTESI[int(almak_istenilen_tas[1]) - 1][index] = "*" #Taş alındıktan sonra yerine boş olarak gözükmesi için yıldız görülüyor.
                oyun_alani_devamini_ciz(OYUN_LISTESI)
                siyahlarin_konumlari.remove(almak_istenilen_tas)
            else:
                print("Lütfen geçerli bir değer giriniz!")
    for i in range(1, siyah_kare_sayilari + 1):
        devam = "e"
        while devam == "e":
            almak_istenilen_tas = input("Almak istediğiniz beyaz taşın konumunu giriniz:")
            almak_istenilen_tas = almak_istenilen_tas.upper()
            if almak_istenilen_tas in siyahlarin_alabilecegi_taslar:
                devam = "H"
                index=degerbul(almak_istenilen_tas[0])
                OYUN_LISTESI[int(almak_istenilen_tas[1]) - 1][index] = "*"
                oyun_alani_devamini_ciz(OYUN_LISTESI)
                beyazlarin_konumlari.remove(almak_istenilen_tas)
            else:
                print("Lütfen geçerli bir değer giriniz!")
tas_sil(BEYAZ_KARE_SAYISI, SIYAH_KARE_SAYISI,BEYAZ_KARELERI_OLUSTURAN_TASLARIN_KONUMLARI,SIYAH_KARELERI_OLUSTURAN_TASLARIN_KONUMLARI)
def hareket_ettir(tas_rengi): #Kullanıcıdan belli bir doğrultuda önünde taş olmaması ve çapraz gitmemesi koşuluyla hareket etmesini sağlayan fonksiyon.
    devam = "e"
    while devam == "e":
        beyaz_kare_say1,siyah_kare_say1,BEYAZ_KARELERI_OLUSTURAN_TASLARIN_KONUMLARI1,SIYAH_KARELERI_OLUSTURAN_TASLARIN_KONUMLARI1= kare_bul(OYUN_LISTESI) #Burada aldığımız değerler hamle yapmadan önceki değerleri gösteriyor.
        try:
            tasin_ve_hareket_edilecek_yerin_konumu = input(
                "Hareket etmesini istediğiniz taşın ve hareket edilecek yerin konumunu giriniz:")
            tasin_ve_hareket_edilecek_yerin_konumu = tasin_ve_hareket_edilecek_yerin_konumu.upper()
            tasin_sutununun_indexi = degerbul(tasin_ve_hareket_edilecek_yerin_konumu[0])
            tasin_satirinin_indexi = int(tasin_ve_hareket_edilecek_yerin_konumu[1]) - 1
            tasin_hareket_etmek_istedigi_yerin_sutununun_indexi = degerbul(tasin_ve_hareket_edilecek_yerin_konumu[3])
            tasin_hareket_etmek_istedigi_yerin_satirinin_indexi = int(tasin_ve_hareket_edilecek_yerin_konumu[4]) - 1
            tasin_gitmek_istedigi_yerin_ismi = tasin_ve_hareket_edilecek_yerin_konumu[3] + \
                                               tasin_ve_hareket_edilecek_yerin_konumu[4]
            tasin_su_anki_konumunun_ismi = tasin_ve_hareket_edilecek_yerin_konumu[0] + \
                                           tasin_ve_hareket_edilecek_yerin_konumu[1]
            gidilebilecek_yerler = []
            if tasin_satirinin_indexi==tasin_hareket_etmek_istedigi_yerin_satirinin_indexi and tasin_sutununun_indexi<tasin_hareket_etmek_istedigi_yerin_sutununun_indexi:
                say=-1 #Sağa gitmeyi kontrol eden yer.
                for i in OYUN_LISTESI[tasin_satirinin_indexi]:
                    say += 1
                    sutun_ismi = harfbul(say)
                    if say > tasin_sutununun_indexi:
                        if i == "*":
                            gidilebilecek_yerler.append(sutun_ismi + tasin_ve_hareket_edilecek_yerin_konumu[1])
                        else:
                            break
            elif tasin_satirinin_indexi==tasin_hareket_etmek_istedigi_yerin_satirinin_indexi and tasin_sutununun_indexi>tasin_hareket_etmek_istedigi_yerin_sutununun_indexi:
                for i in range(SUTUN_SAYISI - 1, -1, -1): #Sola gitmeyi kontrol eden yer.
                    if i < tasin_sutununun_indexi:
                        if OYUN_LISTESI[tasin_satirinin_indexi][i] == "*":
                            gidilebilecek_yerler.append(harfbul(i) + str(tasin_su_anki_konumunun_ismi[1]))
                        else:
                            break
            elif tasin_sutununun_indexi==tasin_hareket_etmek_istedigi_yerin_sutununun_indexi and tasin_satirinin_indexi<tasin_hareket_etmek_istedigi_yerin_satirinin_indexi:
                for i in range(tasin_satirinin_indexi + 1, SATIR_SAYISI): #Aşağı gitmeyi kontrol eden yer.
                    if OYUN_LISTESI[i][tasin_sutununun_indexi] == "*":
                        gidilebilecek_yerler.append(tasin_su_anki_konumunun_ismi[0] + str(i + 1))
                    else:
                        break
            elif tasin_sutununun_indexi==tasin_hareket_etmek_istedigi_yerin_sutununun_indexi and tasin_satirinin_indexi>tasin_hareket_etmek_istedigi_yerin_satirinin_indexi:
                for i in range(SATIR_SAYISI - 1, -1, -1): #Yukarı gitmeyi kontrol eden yer.
                    if i < tasin_satirinin_indexi:
                        if OYUN_LISTESI[i][tasin_sutununun_indexi] == "*":
                            gidilebilecek_yerler.append(tasin_su_anki_konumunun_ismi[0] + str(i + 1))
                        else:
                            break
            if tasin_gitmek_istedigi_yerin_ismi in gidilebilecek_yerler and OYUN_LISTESI[tasin_satirinin_indexi][ #Taşın geldiği yerin ve gidilecek yerin doğru olup olmadığını kontrol eden yer.
                tasin_sutununun_indexi] == tas_rengi and len(tasin_ve_hareket_edilecek_yerin_konumu) == 5:
                devam = "h"
                OYUN_LISTESI[tasin_satirinin_indexi][tasin_sutununun_indexi] = "*"
                OYUN_LISTESI[tasin_hareket_etmek_istedigi_yerin_satirinin_indexi][
                    tasin_hareket_etmek_istedigi_yerin_sutununun_indexi] = tas_rengi
                if tas_rengi == "B":
                    beyazlarin_konumlari.remove(tasin_su_anki_konumunun_ismi)
                    beyazlarin_konumlari.append(tasin_gitmek_istedigi_yerin_ismi)
                else:
                    siyahlarin_konumlari.remove(tasin_su_anki_konumunun_ismi)
                    siyahlarin_konumlari.append(tasin_gitmek_istedigi_yerin_ismi)
            else:
                print("Lütfen geçerli bir değer giriniz")
            print("", end="")
        except:
            print("Lütfen geçerli bir değer giriniz")
    oyun_alani_devamini_ciz(OYUN_LISTESI)
    beyaz_kare_say2,siyah_kare_say2,BEYAZ_KARELERI_OLUSTURAN_TASLARIN_KONUMLARI2,SIYAH_KARELERI_OLUSTURAN_TASLARIN_KONUMLARI2 = kare_bul(OYUN_LISTESI)
    if tas_rengi == "B": #Kare bul fonksiyonunu çağırarak kare oluşup oluşmadığını kontrol ediyoruz ve eğer oluştuysa oyuncuya karşıdan taş alma hakkı tanıyoruz.
        if (beyaz_kare_say1<beyaz_kare_say2) or (beyaz_kare_say2==beyaz_kare_say1 and BEYAZ_KARELERI_OLUSTURAN_TASLARIN_KONUMLARI1!=BEYAZ_KARELERI_OLUSTURAN_TASLARIN_KONUMLARI2) or (beyaz_kare_say2<beyaz_kare_say1 and [tasin_hareket_etmek_istedigi_yerin_satirinin_indexi,tasin_hareket_etmek_istedigi_yerin_sutununun_indexi] in BEYAZ_KARELERI_OLUSTURAN_TASLARIN_KONUMLARI2):
            tas_sil(1,0,BEYAZ_KARELERI_OLUSTURAN_TASLARIN_KONUMLARI2,SIYAH_KARELERI_OLUSTURAN_TASLARIN_KONUMLARI2)
    else:
        if (siyah_kare_say1<siyah_kare_say2) or (siyah_kare_say1==siyah_kare_say2 and SIYAH_KARELERI_OLUSTURAN_TASLARIN_KONUMLARI1!=SIYAH_KARELERI_OLUSTURAN_TASLARIN_KONUMLARI2) or (siyah_kare_say2<siyah_kare_say1 and [tasin_hareket_etmek_istedigi_yerin_satirinin_indexi,tasin_hareket_etmek_istedigi_yerin_sutununun_indexi] in SIYAH_KARELERI_OLUSTURAN_TASLARIN_KONUMLARI2):
            tas_sil(0,1,BEYAZ_KARELERI_OLUSTURAN_TASLARIN_KONUMLARI2,SIYAH_KARELERI_OLUSTURAN_TASLARIN_KONUMLARI2)
def main():
    BEYAZ_TAS_SAYISI = SUTUN_SAYISI * SATIR_SAYISI / 2
    SIYAH_TAS_SAYISI = SUTUN_SAYISI * SATIR_SAYISI / 2
    HAMLE=-1
    while BEYAZ_TAS_SAYISI > 3 and SIYAH_TAS_SAYISI > 3: #3 taş kalana kadar oyun devam ediyor ve 3 taşı kalan oyuncu oyunu kaybetmiş oluyor.
        HAMLE+=1
        if HAMLE%2==0: #Hamle sırasının kimde olduğunu kontrol ettiğimiz yer.
            hareket_ettir("B")
        else:
            hareket_ettir("S")
        beyaz_taslar=[]
        siyah_taslar=[]
        for i in OYUN_LISTESI:
            for j in i:
                if j == "B":
                    beyaz_taslar.append(j)
                elif j == "S":
                    siyah_taslar.append(j)
        BEYAZ_TAS_SAYISI=len(beyaz_taslar)
        SIYAH_TAS_SAYISI=len(siyah_taslar)
        if BEYAZ_TAS_SAYISI==3:
            print("Siyah oyuncu kazandı!")
        elif SIYAH_TAS_SAYISI==3:
            print("Beyaz oyuncu kazandı!")
main()