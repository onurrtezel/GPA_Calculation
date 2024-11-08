import tkinter as tk
from tkinter import messagebox

def vize():
    toplam = 0
    for i in range(1, 3):
        vize_notu = int(vize_entry[i-1].get())
        toplam += vize_notu
    ortalama = toplam / 2
    vize_sonuc_label.config(text=f"Vize Ortalama: {ortalama}")
    return ortalama

def final():
    toplamm = 0
    for i in range(1, 3):
        final_notu = int(final_entry[i-1].get())
        toplamm += final_notu
    ortalamaa = toplamm / 2
    final_sonuc_label.config(text=f"Final Ortalama: {ortalamaa}")
    return ortalamaa

def hesapla():
    try:
        sonuc1 = vize()
        sonuc2 = final()
        genelort = float(((sonuc1 * 40) / 100) + ((sonuc2 * 60) / 100))
        genel_ort_label.config(text=f"Genel Ortalama: {genelort}")
        messagebox.showinfo("Genel Ortalama", f"Genel Ortalama: {genelort}")
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli bir sayı giriniz!")

root = tk.Tk()
root.title("Not Hesaplama")
root.geometry("300x300")

vize_label = tk.Label(root, text="Vize Notları:")
vize_label.pack()

vize_entry = [tk.Entry(root) for _ in range(2)]
for entry in vize_entry:
    entry.pack()

vize_sonuc_label = tk.Label(root, text="Vize Ortalama: ")
vize_sonuc_label.pack()

final_label = tk.Label(root, text="Final Notları:")
final_label.pack()

final_entry = [tk.Entry(root) for _ in range(2)]
for entry in final_entry:
    entry.pack()

final_sonuc_label = tk.Label(root, text="Final Ortalama: ")
final_sonuc_label.pack()

genel_ort_label = tk.Label(root, text="Genel Ortalama: ")
genel_ort_label.pack()

hesapla_button = tk.Button(root, text="Hesapla", command=hesapla)
hesapla_button.pack()

root.mainloop()
