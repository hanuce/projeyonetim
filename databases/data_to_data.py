import pandas as pd
import sqlite3
import os


# Yürütülen dosyanın dizinini al
current_directory = os.path.dirname(os.path.abspath(__file__))

# Çalışma dizinini ayarla
os.chdir(current_directory)

# CSV dosyasının yolu
csv_file_path = 'abilities.csv'  # CSV dosyanızın adını buraya yazın

# SQLite veritabanı dosyasının yolu
sqlite_db_path = 'users.db'  # SQLite veritabanı dosyanızın adını buraya yazın

# CSV dosyasını oku
# İlk 5 sütunu almak için usecols parametresini kullanıyoruz
df = pd.read_csv(csv_file_path, encoding='utf-8', usecols=[0,1,2])

# SQLite veritabanına bağlan
conn = sqlite3.connect(sqlite_db_path)

# DataFrame'i SQLite veritabanına ekle
# 'my_table' adında bir tablo oluşturacak
df.to_sql('abilities', conn, if_exists='append', index=False)

# Bağlantıyı kapat
conn.close()

print("işlem tamam")