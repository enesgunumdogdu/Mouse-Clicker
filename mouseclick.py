import pyautogui
import time
import tkinter as tk

def mouse_tikla():
    try:
        saat = int(saat_entry.get())
        dakika = int(dakika_entry.get())
        saniye = int(saniye_entry.get())
        salise = int(salise_entry.get())
        
        # Tıklama yapılacak zaman alınıyor
        hedef_zaman = (saat, dakika, saniye, salise)
        
        # Girilen zamana ölçekleyebilmek için şimdiki zamanı alıyorum.
        simdiki_zaman = time.localtime()
        
        hedef_zaman_saniye = (hedef_zaman[0] * 3600 + hedef_zaman[1] * 60 + hedef_zaman[2]) + (hedef_zaman[3] / 100)
        simdiki_zaman_saniye = (simdiki_zaman.tm_hour * 3600 + simdiki_zaman.tm_min * 60 + simdiki_zaman.tm_sec) + (time.time() * 100 % 100) / 100
        
        # Belirtilen zamana kadar bekleyin
        while simdiki_zaman_saniye < hedef_zaman_saniye:
            simdiki_zaman = time.localtime()
            simdiki_zaman_saniye = (simdiki_zaman.tm_hour * 3600 + simdiki_zaman.tm_min * 60 + simdiki_zaman.tm_sec) + (time.time() * 100 % 100) / 100
        
        # Mouse'un bulunduğu yere tıklayın
        mouse_x, mouse_y = pyautogui.position()
        pyautogui.click(x=mouse_x, y=mouse_y)
        
        sonuc_label.config(text="Mouse başarıyla tıklandı")
    
    except ValueError:
        sonuc_label.config(text="Girdiğiniz zaman aralığı geçersiz. Lütfen geçerli bir saat, dakika, saniye ve salise girin.")

# Burası kodumuzun grafik arayüz kısmını oluşturuyor.
arayuz = tk.Tk()
arayuz.title("Mouse Tıklama Programı")
arayuz.geometry("550x400")

# Burada kodda girilecek saat, dakika, saniye ve salise değişkenleri kullanıcıdan alınıyor.
saat_label = tk.Label(arayuz, text="Saat:")
saat_label.pack()
saat_entry = tk.Entry(arayuz)
saat_entry.pack()

dakika_label = tk.Label(arayuz, text="Dakika:")
dakika_label.pack()
dakika_entry = tk.Entry(arayuz)
dakika_entry.pack()

saniye_label = tk.Label(arayuz, text="Saniye:")
saniye_label.pack()
saniye_entry = tk.Entry(arayuz)
saniye_entry.pack()

salise_label = tk.Label(arayuz, text="Salise:")
salise_label.pack()
salise_entry = tk.Entry(arayuz)
salise_entry.pack()

# Tıklama yapma butonunu ekledim.
tiklama_button = tk.Button(arayuz, text="Tıklama Yap", command=mouse_tikla)
tiklama_button.pack()

# Tıklama yapıldı veya yapılmadı sonucu burada görüntülenecek.
sonuc_label = tk.Label(arayuz, text="")
sonuc_label.pack()

arayuz.mainloop()
