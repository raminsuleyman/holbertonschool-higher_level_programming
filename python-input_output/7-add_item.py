#!/usr/bin/python3
"""add item"""
import sys
import os


# Əvvəlki tapşırıqlardakı funksiyaları import edirik
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# 1. Əgər fayl mövcuddursa, mövcud siyahını oxuyuruq
if os.path.exists(filename):
    items = load_from_json_file(filename)
else:
    # 2. Fayl yoxdursa, boş bir siyahı ilə başlayırıq
    items = []

# 3. Komanda sətrindən gələn arqumentləri siyahıya əlavə edirik
# sys.argv[1:] proqramın adından sonra gələn bütün sözləri götürür
items.extend(sys.argv[1:])

# 4. Yenilənmiş siyahını yenidən fayla yazırıq
save_to_json_file(items, filename)
