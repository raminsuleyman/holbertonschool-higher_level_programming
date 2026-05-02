#!/usr/bin/python3
"""basic serialization"""
import json


def serialize_and_save_to_file(data, filename):
    """json formatina cevirir ve fayla yzir"""
    with open(filename, "w") as f:
        f.write(json.dumps(data))

def load_and_deserialize(filename):
    """json faylini oxuyur"""
    with open(filename, "r") as f:
        data = f.read()
        return json.loads(data)
