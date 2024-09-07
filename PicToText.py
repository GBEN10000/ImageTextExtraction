from PIL import Image
import pytesseract
import cv2
import numpy as np

# Path to the Tesseract executable (change this based on your installation)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_selected_numbers(image_path):
    try:
        # Open the image file
        img = Image.open(image_path)

        # Convert PIL Image to OpenCV format
        img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

        # Convert to grayscale
        gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)

        # Apply adaptive thresholding
        _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

        # Use pytesseract to do OCR on the processed image
        text = pytesseract.image_to_string(thresh, config='--oem 1 --psm 6 outputbase digits')

        # Extracted numbers
        selected_numbers = [int(s) for s in text.split() if s.isdigit()]

        return selected_numbers

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
image_path = r'C:\Users\Dell\Desktop\MY PROJECTS\NUMB.jpg'
result = extract_selected_numbers(image_path)

if result is not None:
    print("Selected Numbers:", result)
