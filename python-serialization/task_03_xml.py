#!/usr/bin/python3

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary into XML and save it to the given filename.

    Parameters:
    dictionary (dict): The dictionary to serialize.
    filename (str): The name of the file to save the serialized XML data.
    """
    # Create the root element
    root = ET.Element("data")

    """Iterate through the dictionary items and add them as
    child elements to the root"""
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    """Create an ElementTree object and write it to the
    provided filename"""
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """
    Read XML data from the given file and return a deserialized
    Python dictionary.

    Parameters:
    filename (str): The name of the file to read the XML data
    from.

    Returns:
    dict: The deserialized Python dictionary.
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    
    dict = {}
    # Navigate through the XML elements to reconstruct the dictionary
    for child in root:
        dict[child.tag] = child.text

    return dict
