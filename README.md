#  Doktor & Hekim Randevu ve Hasta Takip Sistemi

Bu proje, Python dili ve Tkinter kütüphanesi kullanılarak geliştirilmiş bir **randevu ve hasta takip otomasyonudur**. Doktor & hekimlerin hasta bilgilerini kaydedebileceği, randevu oluşturabileceği ve bu randevulara özel notlar alabileceği kullanıcı dostu bir arayüz sunar.

---

## 🚀 Özellikler

- 🧾 **Hasta Kayıt**: İsim, soyisim, doğum tarihi, telefon ve randevu tarihi gibi bilgilerle hasta kaydı yapılır.  
- 📋 **Randevu Listesi**: Tüm randevular tablo olarak görüntülenir.  
- 📝 **Randevuya Not Ekleme**: Seçilen randevulara özel açıklamalar girilebilir ve kaydedilebilir.  
- 🗑️ **Randevu Silme**: Yanlış ya da iptal edilen randevular sistemden kolayca silinir.  
- 📤 **Günlük PDF Raporu**: Belirli bir tarihteki randevular PDF formatında dışa aktarılabilir.  

--- 
## 📂 Dosya Yapısı
├── main.py                # Ana uygulama arayüzü

├── data_handler.py        # CSV işlemleri (kayıt, silme, güncelleme)

├── pdf_generator.py       # PDF oluşturma fonksiyonları

├── patients.csv           # Hasta veritabanı (otomatik oluşturulur)

└── README.md              # Proje açıklaması
---

## 🛠️ Teknolojiler

- **Python 3.x**
- **Tkinter** – Grafiksel kullanıcı arayüzü  
- **Pandas** – CSV veritabanı işlemleri  
- **ReportLab** – PDF raporu oluşturma  

---

## 📦 Gerekli Kütüphaneler

Bu projeyi çalıştırmadan önce aşağıdaki kütüphanelerin sisteminizde kurulu olması gerekmektedir:

```bash
pip install pandas reportlab
