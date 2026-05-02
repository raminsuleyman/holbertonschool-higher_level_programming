#!/usr/bin/python3
"""load json"""
import json


def load_from_json_file(filename):
    """JSON faylından məlumatı oxuyub Python obyektinə çevirən funksiya"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
