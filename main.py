from core import ocr
from core import utils
# -------------
# testing
# -------------
# get the pdf
pdf_path = './docs/scans.pdf'
# and extract each page and convert it into a jpeg
utils.extract_pages(pdf_path, 'img')

# define image path (here first image)
image_path = 'img/page_0.jpg'
# coordinates from top left
# these can easily be defined using gimp
zones = [
    (240, 900, 1400, 975),
    (237, 2220, 456, 2253)
]

# draw boxes in images for illustration purposes
utils.draw_boxes(image_path, zones, './misc/extraction_zones.jpg')

# if boxes are correct, then perform ocr indexing on them
print(ocr.perform_ocr(input_path=image_path, coordinates=zones))




