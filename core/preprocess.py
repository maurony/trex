import numpy as np
import cv2


def straighten_image(image_path):
    """Straighten the image by rotating it

    Calculates the angle the image has needs to be rotated in order to be straightened out and then applies the affine
    transformation to actually rotate the image

    Args:
        image_path (string): path to image

    Returns:
        rotated image

    """
    # read image
    image = cv2.imread(image_path)

    # convert background to grey
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.bitwise_not(gray)

    # convert all color either to black or white or white
    # i.e. threshold the image, setting all foreground pixels to
    # 255 and all background pixels to 0
    thresh = cv2.threshold(gray, 0, 255,
                           cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # grab the (x, y) coordinates of all pixel values that
    # are greater than zero, then use these coordinates to
    # compute a rotated bounding box that contains all
    # coordinates
    coords = np.column_stack(np.where(thresh > 0))
    angle = cv2.minAreaRect(coords)[-1]

    # the `cv2.minAreaRect` function returns values in the
    # range [-90, 0); as the rectangle rotates clockwise the
    # returned angle trends to 0 -- in this special case we
    # need to add 90 degrees to the angle.
    # essentially defines the side the rectangle will rotate to.
    if angle < -45:
        angle = -(90 + angle)
    # otherwise, just take the inverse of the angle to make it positive
    else:
        angle = -angle

    # rotate the image
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (w, h),
                                   flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

    # draw the correction angle on the image so we can validate it
    # meta_info = "Image has been rotated by: {:.2f} degrees".format(angle)

    # show the output image
    return rotated_image


def gaussian_blur(image_path):
    """Straighten the image by rotating it

    Calculates the angle the image has needs to be rotated in order to be straightened out and then applies the affine
    transformation to actually rotate the image

    Args:
        image_path (string): path to image

    Returns:
        rotated image

    """
    img = cv2.imread(image_path)

    # apply GaussianBlur to smooth image
    blur = cv2.GaussianBlur(img, (5, 3), 1)

    # threshold gray region to white (255,255, 255) and sets the rest to black(0,0,0)
    mask = cv2.inRange(blur, (0, 0, 0), (150, 150, 150))

    # invert the image to have text black-in-white
    return 255 - mask


def median_blur(image_path):
    """Straighten the image by rotating it

    Calculates the angle the image has needs to be rotated in order to be straightened out and then applies the affine
    transformation to actually rotate the image

    Args:
        image_path (string): path to image

    Returns:
        rotated image

    """
    img = cv2.imread(image_path)

    # apply MedianBlur to smooth image
    blur = cv2.medianBlur(img, 3)

    # threshold gray region to white (255,255, 255) and sets the rest to black(0,0,0)
    #mask = cv2.inRange(blur, (0, 0, 0), (150, 100, 100))

    # invert the image to have text black-in-white
    return blur

