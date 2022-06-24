"""
A small utility script to convert the Pascal VOC labels from andrewmvd/car-plate-detection to YOLO labels
"""

import xml.etree.ElementTree as ET
import os

for annotation_file in os.listdir("annotations"):
    tree = ET.parse("annotations/" + annotation_file)
    root = tree.getroot()
    size = root.find("size")
    img_width = int(size.find("width").text)
    img_height = int(size.find("height").text)
    depth = int(size.find("depth").text)
    assert depth == 3
    for obj in root.findall("object"):
        name = obj.find("name").text
        assert name == "licence"
        bndbox = obj.find("bndbox")
        xmin = int(bndbox.find("xmin").text)
        xmax = int(bndbox.find("xmax").text)
        ymin = int(bndbox.find("ymin").text)
        ymax = int(bndbox.find("ymax").text)
        print(xmin, ymin, xmax, ymax)
        x_center = xmin + (xmax-xmin)//2
        y_center = ymin + (ymax-ymin)//2
        width = xmax - xmin
        height = ymax - ymin
        assert (height > 0 and width > 0), f"Invalid dimensions for {annotation_file}"
        x_center_normalized = x_center / img_width
        y_center_normalized = y_center / img_height
        width_normalized = width / img_width
        height_normalized = height / img_height
        with open("labels/" + annotation_file.replace(".xml", ".txt"), "a") as f:
            f.write(f"0 {x_center_normalized} {y_center_normalized} {width_normalized} {height_normalized}\n")