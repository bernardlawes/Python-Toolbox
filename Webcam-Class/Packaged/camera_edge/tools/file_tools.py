# my_app/tools/file_tools.py

import os
import cv2

def save_image(image, path, filename):
    os.makedirs(path, exist_ok=True)
    full_path = os.path.join(path, filename)
    success = cv2.imwrite(full_path, image)
    return success, full_path

def list_images(directory, ext=".png"):
    return [f for f in os.listdir(directory) if f.endswith(ext)]
