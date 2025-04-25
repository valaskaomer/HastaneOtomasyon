import pandas as pd
import os

CSV_FILE = 'patients.csv'
COLUMNS = ['Ad', 'Soyad', 'Doğum Tarihi', 'Telefon', 'Randevu Tarihi', 'Notlar']

def load_data():
    if not os.path.exists(CSV_FILE):
        pd.DataFrame(columns=COLUMNS).to_csv(CSV_FILE, index=False)
    df = pd.read_csv(CSV_FILE)
    if 'Notlar' not in df.columns:
        df['Notlar'] = ""
    return df

def save_data(new_record):
    df = load_data()
    df = pd.concat([df, pd.DataFrame([new_record])], ignore_index=True)
    df.to_csv(CSV_FILE, index=False)

def filter_by_date(date):
    df = load_data()
    return df[df['Randevu Tarihi'] == date]

def update_note(index, note):
    df = load_data()
    df.at[index, 'Notlar'] = note
    df.to_csv(CSV_FILE, index=False)

def delete_record(index):
    df = load_data()
    if index in df.index:
        df = df.drop(index)
        df.to_csv(CSV_FILE, index=False)
