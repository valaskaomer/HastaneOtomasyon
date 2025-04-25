import tkinter as tk
from tkinter import messagebox, ttk
from data_handler import load_data, save_data, update_note
from pdf_generator import generate_daily_pdf
from data_handler import delete_record
import os

root = tk.Tk()
root.title("Doktor ve Hekim Randevu ve Hasta Takip Sistemi")
root.geometry("900x600")

# 📌 Kayıt Formu
frame_kayit = tk.LabelFrame(root, text="Hasta Kayıt Formu", padx=10, pady=10)
frame_kayit.pack(fill="x", padx=10, pady=5)

tk.Label(frame_kayit, text="Ad").grid(row=0, column=0)
tk.Label(frame_kayit, text="Soyad").grid(row=0, column=2)
tk.Label(frame_kayit, text="Doğum Tarihi").grid(row=1, column=0)
tk.Label(frame_kayit, text="Telefon").grid(row=1, column=2)
tk.Label(frame_kayit, text="Randevu Tarihi (GG/AA/YYYY)").grid(row=2, column=0)

entry_ad = tk.Entry(frame_kayit)
entry_soyad = tk.Entry(frame_kayit)
entry_dogum = tk.Entry(frame_kayit)
entry_telefon = tk.Entry(frame_kayit)
entry_randevu = tk.Entry(frame_kayit)

entry_ad.grid(row=0, column=1)
entry_soyad.grid(row=0, column=3)
entry_dogum.grid(row=1, column=1)
entry_telefon.grid(row=1, column=3)
entry_randevu.grid(row=2, column=1)

def hasta_kaydet():
    ad = entry_ad.get()
    soyad = entry_soyad.get()
    dogum = entry_dogum.get()
    telefon = entry_telefon.get()
    randevu = entry_randevu.get()

    if not (ad and soyad and dogum and telefon and randevu):
        messagebox.showerror("Hata", "Tüm alanlar doldurulmalı.")
        return

    kayit = {
        "Ad": ad,
        "Soyad": soyad,
        "Doğum Tarihi": dogum,
        "Telefon": telefon,
        "Randevu Tarihi": randevu,
        "Notlar": ""
    }
    save_data(kayit)
    messagebox.showinfo("Başarılı", "Kayıt başarıyla eklendi.")
    listeyi_guncelle()

tk.Button(frame_kayit, text="Kaydet", command=hasta_kaydet).grid(row=3, column=1, pady=5)

# 📅 Randevu Listesi
frame_liste = tk.LabelFrame(root, text="Randevu Listesi", padx=10, pady=10)
frame_liste.pack(fill="both", expand=True, padx=10, pady=5)

tree = ttk.Treeview(frame_liste, columns=("Ad", "Soyad", "Doğum", "Telefon", "Randevu", "Notlar"), show="headings")
for col in tree["columns"]:
    tree.heading(col, text=col)
    tree.column(col, width=130)
tree.pack(fill="both", expand=True)

def listeyi_guncelle():
    for i in tree.get_children():
        tree.delete(i)
    for index, row in load_data().iterrows():
        tree.insert("", "end", iid=index, values=list(row))

listeyi_guncelle()

# 📝 Not Yazma Alanı
frame_not = tk.LabelFrame(root, text="Randevu Notu", padx=10, pady=10)
frame_not.pack(fill="x", padx=10, pady=5)

text_not = tk.Text(frame_not, height=5)
text_not.pack(fill="x")

btn_not_kaydet = tk.Button(frame_not, text="Notu Kaydet", command=lambda: notu_kaydet())
btn_not_kaydet.pack(pady=5)

secilen_index = None

def randevu_sec(event):
    global secilen_index
    selected = tree.focus()
    if not selected:
        return
    secilen_index = int(selected)
    df = load_data()
    not_metni = df.loc[secilen_index, 'Notlar']
    text_not.delete("1.0", tk.END)
    text_not.insert(tk.END, not_metni)

def notu_kaydet():
    global secilen_index
    if secilen_index is None:
        messagebox.showwarning("Uyarı", "Lütfen önce bir randevu seçin.")
        return
    metin = text_not.get("1.0", tk.END).strip()
    update_note(secilen_index, metin)
    messagebox.showinfo("Başarılı", "Not kaydedildi.")
    listeyi_guncelle()
# Randevu Silme
def randevu_sil():
    global secilen_index
    if secilen_index is None:
        messagebox.showwarning("Uyarı", "Lütfen silmek için bir randevu seçin.")
        return
    cevap = messagebox.askyesno("Onay", "Bu randevuyu silmek istediğinize emin misiniz?")
    if cevap:
        delete_record(secilen_index)
        messagebox.showinfo("Silindi", "Randevu başarıyla silindi.")
        secilen_index = None
        text_not.delete("1.0", tk.END)
        listeyi_guncelle()
tree.bind("<<TreeviewSelect>>", randevu_sec)

# 📤 PDF Oluşturma Alanı
frame_pdf = tk.Frame(root)
frame_pdf.pack(pady=5)

tk.Label(frame_pdf, text="PDF Tarih (GG/AA/YYYY):").pack(side="left")
entry_pdf_tarih = tk.Entry(frame_pdf)
entry_pdf_tarih.pack(side="left", padx=5)

def pdf_olustur():
    tarih = entry_pdf_tarih.get()
    if not tarih:
        messagebox.showerror("Hata", "Lütfen tarih girin (GG/AA/YYYY).")
        return
    try:
        filename = generate_daily_pdf(tarih)
        if filename:
            messagebox.showinfo("Başarılı", f"PDF oluşturuldu: {filename}")
            os.startfile(filename)
        else:
            messagebox.showwarning("Sonuç Yok", "Belirtilen tarihte kayıt bulunamadı.")
    except Exception as e:
        messagebox.showerror("Hata", f"PDF oluşturulamadı.\n{str(e)}")

btn_gunluk_pdf = tk.Button(frame_pdf, text="Günlük PDF", command=pdf_olustur)
btn_gunluk_pdf.pack(side="left", padx=5)
btn_sil = tk.Button(root, text="Seçilen Randevuyu Sil", fg="white", bg="red", command=lambda: randevu_sil())
btn_sil.pack(pady=5)

root.mainloop()
