import csv
import os
import pickle

# Yürütülen dosyanın dizinini al
current_directory = os.path.dirname(os.path.abspath(__file__))

# Çalışma dizinini ayarla
os.chdir(current_directory)

# CSV dosyasını okuyup sözlük yapısına dönüştüren fonksiyon
def csv_to_dict(file_path):
    branches_dict = {}
    
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Başlık satırını atla
        for row in reader:
            branch_id = int(row[0])  # branch_id'yi integer'a dönüştür
            branch_detail = row[1]
            
            # branch_id anahtar, branch_detail value
            branches_dict[branch_id] = branch_detail
    
    return branches_dict

# Sözlüğü txt dosyasına kaydetme
def save_dict_to_txt(data, output_file):
    with open(output_file, mode='w', encoding='utf-8') as file:
        file.write(str(data))  # Sözlüğü string olarak kaydet

# Txt dosyasını okuyup sözlüğe dönüştürme
def load_dict_from_txt(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        content = file.read()
        return eval(content)  # String'i Python sözlüğüne dönüştür

# CSV dosyasının yolu
file_path = 'teacher_branches.csv'

# CSV'yi sözlüğe dönüştür
branches_dict = csv_to_dict(file_path)

# Kaydedilecek txt dosyasının adı
output_file = 'branches_dict.txt'

# Sözlüğü txt dosyasına kaydet
save_dict_to_txt(branches_dict, output_file)



