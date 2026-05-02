#!/usr/bin/python3
"""This module is for serialization tasks."""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to an XML file.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        item = ET.SubElement(root, "item")
        item.set("key", str(key))

        # Store type information
        item.set("type", type(value).__name__)
        item.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserialize an XML file back into a Python dictionary.
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    result = {}

    for item in root.findall("item"):
        key = item.get("key")
        value = item.text
        value_type = item.get("type")

        # Convert back to original type
        if value_type == "int":
            value = int(value)
        elif value_type == "float":
            value = float(value)
        elif value_type == "bool":
            value = value == "True"
        elif value_type == "NoneType":
            value = None
        # else: keep as string

        result[key] = value

    return result
