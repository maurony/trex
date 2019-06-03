"""function used to recognise text in images"""

import pytesseract
from PIL import Image


def crop(input_path, coordinates, output_path=None):
    """
    @param input_path: The path to the image to edit
    @param coordinates: A tuple of x/y coordinates (x1, y1, x2, y2)
    @param output_path: Path to save the cropped image
    """
    image_obj = Image.open(input_path)
    cropped_image = image_obj.crop(coordinates)

    if output_path is not None:
        cropped_image.save(output_path)
    else:
        return cropped_image


def perform_ocr(input_path, coordinates):
    """
    @param input_path: The path to the image to edit
    @param coordinates: A tuple of x/y coordinates (x1, y1, x2, y2)
    """
    text_list = []
    config = '-l deu --oem 1 --psm 3'
    for coords in coordinates:
        cropped_image = crop(input_path=input_path, coordinates=coords)
        recognized_text = pytesseract.image_to_string(cropped_image, config=config)
        text_list.append(recognized_text)

    return text_list

