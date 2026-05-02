#!/usr/bin/python3
"""csv and json"""


import csv
import json

def convert_csv_to_json(csv_filename):
    """
    CSV faylını oxuyur və onu data.json faylına çevirir.
    Uğurlu olarsa True, xəta baş verərsə False qaytarır.
    """
    try:
        # 1. CSV faylını açırıq və oxuyuruq
        with open(csv_filename, mode='r', encoding='utf-8') as csv_f:
            # DictReader hər sətri sütun adları ilə açar-dəyər (key-value) cütünə çevirir
            csv_reader = csv.DictReader(csv_f)
            
            # Bütün lüğətləri (sətirləri) bir siyahıya yığırıq
            data_list = [row for row in csv_reader]

        # 2. JSON faylına yazırıq
        with open('data.json', mode='w', encoding='utf-8') as json_f:
            # indent=4 məlumatın JSON-da daha səliqəli və oxunaqlı görünməsini təmin edir
            json.dump(data_list, json_f, indent=4)

        return True

    except FileNotFoundError:
        # Fayl tapılmadıqda False qaytarırıq
        print(f"Xəta: '{csv_filename}' faylı tapılmadı.")
        return False
    except Exception as e:
        # Digər gözlənilməz xətalar üçün
        print(f"Gözlənilməz xəta baş verdi: {e}")
        return False
