from core import ocr, utils, preprocess, table
from itertools import chain
import cv2
import os
import numpy as np
import json
# -------------
# testing
# -------------

if __name__ == '__main__':
    with open('input.json') as json_file:
        template = json.load(json_file)

    document_path = template['document_path']
    classification_bbox = template['classification_bbox']

    names = []
    bounding_boxes = []
    for box in template['bounding_boxes']:
        names.append(box['name'])
        bounding_boxes.append(tuple(box['bbox']))

    # draw boxes in images for illustration purposes
    utils.draw_boxes(document_path, bounding_boxes, './misc/extraction_zones.jpg')
    img = cv2.GaussianBlur(cv2.imread(document_path), (5, 5), 0)
    # if boxes are correct, then perform ocr indexing on them
    print(ocr.perform_ocr(input_path=document_path, coordinates=bounding_boxes))

# get the pdf
#pdf_path = './docs/scans.pdf'
# and extract each page and convert it into a jpeg
#utils.extract_pages(pdf_path, 'img')