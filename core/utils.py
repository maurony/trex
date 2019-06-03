import pdf2image as pi
from PIL import Image, ImageDraw


def extract_pages(input_path, destination_directory):
    """
    @param input_path: file with multiple pages
    @param destination_directory: directory to save destination images
    """
    pages = pi.convert_from_path(input_path)
    for i in range(len(pages)):
        pages[i].save("./{0}/page_{1}.jpg".format(destination_directory, i), 'JPEG')


def draw_boxes(input_path, coordinates, output_path):
    """
    @param input_path: The path to the image to edit
    @param coordinates: An array of tuples of x/y coordinates (x1, y1, x2, y2)
    @param output_path: Path to save the drawn image
    """
    img = Image.open(input_path)
    draw = ImageDraw.Draw(img)
    for coords in coordinates:
        draw.rectangle(coords, outline=(255, 0, 0, 255), width=3)

    del draw
    img.save(output_path)
