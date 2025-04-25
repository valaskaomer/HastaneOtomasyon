from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from data_handler import filter_by_date

def create_pdf(dataframe, filename):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4
    c.setFont("Helvetica", 12)
    y = height - 50
    c.drawString(50, y, f"Randevu Raporu: {filename}")
    y -= 30

    for _, row in dataframe.iterrows():
        line1 = f"{row['Ad']} {row['Soyad']} - {row['Doğum Tarihi']} - {row['Telefon']} - {row['Randevu Tarihi']}"
        line2 = f"Not: {row['Notlar']}"
        c.drawString(50, y, line1)
        y -= 20
        c.drawString(70, y, line2)
        y -= 30
        if y < 50:
            c.showPage()
            c.setFont("Helvetica", 12)
            y = height - 50

    c.save()

def generate_daily_pdf(tarih):
    df = filter_by_date(tarih)
    if df.empty:
        return None
    filename = f"randevu_gunluk_{tarih.replace('/', '-')}.pdf"
    create_pdf(df, filename)
    return filename
