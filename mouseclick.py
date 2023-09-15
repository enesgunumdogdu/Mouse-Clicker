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
        
        # Belirtilen saate kadar bekleyin
        while time.localtime().tm_hour < saat:
            pass
        
        # Belirtilen dakikaya kadar bekleyin
        while time.localtime().tm_min < dakika:
            pass
        
        # Belirtilen saniyeye kadar bekleyin
        while time.localtime().tm_sec < saniye:
            pass
        
        # Mouse'un bulunduğu yere tıklayın
        mouse_x, mouse_y = pyautogui.position()
        pyautogui.click(x=mouse_x, y=mouse_y)
        
        sonuc_label.config(text="Mouse başarıyla tıklandı")
    
    except ValueError:
        sonuc_label.config(text="Girdiğiniz zaman aralığı geçersiz.Lütfen geçerli bir saat, dakika, saniye ve salise girin.")

# Burası kodumuzun grafik arayüz kısmını oluşturuyor.
arayuz = tk.Tk()
arayuz.title("Mouse Tıklama Programı - Berat Aras")
arayuz.geometry("550x400")
#arayuz.configure(bg="#0F3D35")

# Burada kodda girilecek saat, saniye, salise değişkenleri kullanıcıdan alınıyor.
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

# Tıklama yapıldı veya yapılmadı sonucu ise burada görüntülenecek.
sonuc_label = tk.Label(arayuz, text="")
sonuc_label.pack()

arayuz.mainloop()
