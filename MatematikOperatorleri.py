# # Öncelikle iki değişken tanımlıyoruz
#
# a = 2
# b = 5
# sonuc = 0
#
#
# # Operatörler =>
#
# # Toplama işlemi => '+'
# sonuc = a+b
# print("Toplama Sonucu => ",sonuc)
#
# # Çıkarma işlemi =>
# sonuc = a-b
# print("Çıkarma Sonucu => ",sonuc)
#
# # Çarpma İşlemi => '*'
# sonuc = a*b
# print("Çarpma Sonucu => ",sonuc)
#
# # Bölme İşlemi => '/'
# sonuc = a/b
# print("Bölme Sonucu => ",sonuc)
#
# # Mod Alma İşlemi => '%'
# sonuc = a%b
# print("Mod Sonucu => ",sonuc)
#
#
# # Örnekler
# # İnput metodu ile dışarıdan gelen değerleri alabiliriz. int() içerisine ekleyerek gelen sayıların string değil, sayısal bir tipte olduğunu belirtiyoruz.
#
# # int içine alınmadan yazılan hali
#
# sayiBir = input("Lütfen Birinci Sayıyı Giriniz :")
# sayiIki = input("Lütfen İkinci Sayıyı Giriniz: ")
#
# # string toplamasında sayılar yan yana eklenecektir.
#
# print(sayiBir+sayiIki)
#
#
# # int içerisine alarak deniyoruz
#
# sayiBir = int(input("Lütfen Birinci Sayıyı Giriniz :"))
# sayiIki = int(input("Lütfen İkinci Sayıyı Giriniz: "))
#
# print(sayiBir+sayiIki)
#
#
# # Örnek 2=> Dışarıdan alınan iki sayının karelerinin toplamı kaçtır?
#
# sayi1 = int(input("Lütfen bir sayı giriniz : "))
# sayi2 = int(input("Lütfen ikinci sayıyı giriniz : "))
#
# #Birinci Yöntem
#
# sayiBirKaresi = sayi1 * sayi1
# sayiIkiKaresi = sayi2 * sayi2
#
# # İkinci Yöntem
#
# import math # Bu kütüphaneler genelde projenin en tepesinde eklenir. Matematiksel işlemleri daha hızlı gerçekleştirmemz için kullanılan bir kütüphanedir. İçerisinde birçok fonksiyon bulundurur.
#
# sayiBirKaresi= math.pow(sayi1,2)
# sayiIkiKaresi = math.pow(sayi2,2)
#
# # # Math kütüphanesini import ederek projeye ekleyebilir ve math.pow() fonksiyonunu kullanabiliriz. veya üstteki yöntem ile işlemleri gerçekleştirebiliriz.
#
# karelerToplami = sayiBirKaresi + sayiIkiKaresi
#
# print(karelerToplami)
#
# # Örnek 3 => Kullanıcıdan vize ve final notları alınacak. Vizenin yüzde 30'u , finalin yüzde 70'i alınarak son not ekrana yansıtılacak.
#
# vizeNotu = int(input("Lütfen Vize Notunuzu Giriniz: "))
# finalNotu = int(input("Lütfen Final Notunuzu Giriniz: "))
#
# sonuc = (vizeNotu * 0.30) + (finalNotu * 0.70)
# print(sonuc)
#
# # Örnek 4 => Mail Adresi Oluşturma. Kullanıcıdan ad bilgisi alınacak ve geriye ad@hotmail.com.tr cevabı dönülecek.
#
# ad = input("Lütfen Mail Hesap Adınızı Giriniz: ")
# print(ad+"@hotmail.com.tr")
#
# # ----------Atama Operatörleri-----------
#
sayi = 5


# '=' Eşitlik operatörü bir atama operatörüdür. Eşitliğin sağ tarafından gelen değeri sol taraftaki değişkene atama görevini üstlenir.

sayi = sayi + 10
print(sayi) # 15 sonucunu verecektir.

# Aynı işlem şu şekilde kısaltılabilir

sayi += 10
print(sayi)

# Toplama işlemi gibi çıkarma, bölme vb operatörlerimiz de aynı şekilde kısaltılabilir.

sayi -= 10
print(sayi)

sayi *=10
print(sayi)

sayi /=10
print(sayi)

sayi%=10
print(sayi)







