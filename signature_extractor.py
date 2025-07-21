import cv2
import numpy as np
import os

def extract_signature(input_path, output_path):
    # Read the image
    image = cv2.imread(input_path, cv2.IMREAD_COLOR)
    if image is None:
        raise ValueError(f'Could not read image: {input_path}')

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Threshold to create binary mask for signature (tune threshold as needed)
    _, mask = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)

    # Find contours of the signature
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not contours:
        # No signature found, save a transparent image of same size
        h, w = image.shape[:2]
        transparent = np.zeros((h, w, 4), dtype=np.uint8)
        cv2.imwrite(output_path, transparent)
        return output_path

    # Get bounding box of all contours combined
    x, y, w, h = cv2.boundingRect(np.vstack(contours))

    # Crop the image and mask to the bounding box
    cropped_img = image[y:y+h, x:x+w]
    cropped_mask = mask[y:y+h, x:x+w]

    # Prepare alpha channel: signature is opaque, background is transparent
    alpha = cropped_mask

    # Split channels and merge with alpha
    b, g, r = cv2.split(cropped_img)
    png = cv2.merge([b, g, r, alpha])

    # Save as PNG
    cv2.imwrite(output_path, png)
    return output_path
