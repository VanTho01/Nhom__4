import cv2
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk

def normalize_image(img):
    normalized_img = (img - np.min(img)) / (np.max(img) - np.min(img)) * 255
    return np.uint8(normalized_img)

def display_images(rgb_img, grayscale_img, normalized_rgb_img, normalized_gray_img):
    display_image(rgb_img, rgb_label)
    display_image(grayscale_img, grayscale_label)
    display_image(normalized_rgb_img, normalized_rgb_label)
    display_image(normalized_gray_img, normalized_gray_label)

def display_image(img, label):
    tk_image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    tk_image = ImageTk.PhotoImage(image=tk_image)
    label.config(image=tk_image)
    label.image = tk_image

def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.png *.jpeg *.bmp *.gif")])
    if file_path:
        original_rgb_img = cv2.imread(file_path, cv2.IMREAD_COLOR)
        original_gray_img = cv2.cvtColor(original_rgb_img, cv2.COLOR_BGR2GRAY)
        normalized_rgb_img = normalize_image(original_rgb_img)
        normalized_gray_img = normalize_image(original_gray_img)
        display_images(original_rgb_img, original_gray_img, normalized_rgb_img, normalized_gray_img)

app = tk.Tk()
app.title("Image Converter")

frame = ttk.Frame(app)
frame.grid(column=0, row=0, padx=10, pady=10)

open_button = ttk.Button(frame, text="Open Image", command=open_image)
open_button.grid(column=0, row=0)

rgb_label = ttk.Label(app, text="RGB Image")
rgb_label.grid(column=0, row=1)

grayscale_label = ttk.Label(app, text="Grayscale Image")
grayscale_label.grid(column=1, row=1)

normalized_rgb_label = ttk.Label(app, text="Normalized RGB Image")
normalized_rgb_label.grid(column=2, row=1)

normalized_gray_label = ttk.Label(app, text="Normalized Grayscale Image")
normalized_gray_label.grid(column=3, row=1)

app.mainloop()
