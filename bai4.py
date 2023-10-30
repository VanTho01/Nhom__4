import cv2
import numpy as np
import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk

def apply_canny_edge_detection(image, lower_threshold, upper_threshold):
    # Áp dụng thuật toán Canny để tách biên ảnh
    edges = cv2.Canny(image, lower_threshold, upper_threshold)
    return edges

def display_images(original_image, edge_image):
    display_image(original_image, original_label)
    display_image(edge_image, edge_label)

def display_image(img, label):
    tk_image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    tk_image = ImageTk.PhotoImage(image=tk_image)
    label.config(image=tk_image)
    label.image = tk_image

def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.png *.jpeg *.bmp *.gif")])
    if file_path:
        original_img = cv2.imread(file_path, cv2.IMREAD_COLOR)
        update_edge_image(original_img)

def update_edge_image(original_image):
    lower_threshold = int(lower_threshold_var.get())
    upper_threshold = int(upper_threshold_var.get())
    edge_img = apply_canny_edge_detection(original_image, lower_threshold, upper_threshold)
    display_images(original_image, edge_img)

app = tk.Tk()
app.title("Image Edge Detection")

frame = ttk.Frame(app)
frame.grid(column=0, row=0, padx=10, pady=10)

open_button = ttk.Button(frame, text="Open Image", command=open_image)
open_button.grid(column=0, row=0)

original_label = ttk.Label(app, text="Original Image")
original_label.grid(column=0, row=1)

edge_label = ttk.Label(app, text="Edge Detection Image")
edge_label.grid(column=1, row=1)

threshold_frame = ttk.LabelFrame(app, text="Thresholds")
threshold_frame.grid(column=0, row=2)

lower_threshold_label = ttk.Label(threshold_frame, text="Lower Threshold:")
lower_threshold_label.grid(column=0, row=0)
lower_threshold_var = tk.StringVar(value="100")
lower_threshold_entry = ttk.Entry(threshold_frame, textvariable=lower_threshold_var)
lower_threshold_entry.grid(column=1, row=0)

upper_threshold_label = ttk.Label(threshold_frame, text="Upper Threshold:")
upper_threshold_label.grid(column=0, row=1)
upper_threshold_var = tk.StringVar(value="200")
upper_threshold_entry = ttk.Entry(threshold_frame, textvariable=upper_threshold_var)
upper_threshold_entry.grid(column=1, row=1)

update_button = ttk.Button(threshold_frame, text="Update", command=update_edge_image)
update_button.grid(column=0, row=2, columnspan=2)

app.mainloop()
