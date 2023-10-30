import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageProcessingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Processing App")

        self.img = None
        self.filtered_img = None
        self.brightness = 1.0  # Giá trị ban đầu của độ sáng

        self.canvas = tk.Canvas(self.root, width=500, height=450)
        self.canvas.pack()

        self.load_button = tk.Button(self.root, text="Tải Ảnh", command=self.load_image)
        self.load_button.pack()

        self.process_button = tk.Button(self.root, text="Xử lý ảnh", command=self.process_image)
        self.process_button.pack()
        
        # Thêm thanh trượt độ sáng
        self.brightness_scale = tk.Scale(self.root, label="Độ Sáng", from_=0.1, to=2.0, resolution=0.05, orient=tk.HORIZONTAL, command=self.update_brightness)
        self.brightness_scale.set(1.0)  # Giá trị ban đầu
        self.brightness_scale.pack()

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")])
        if file_path:
            self.img = cv2.imread(file_path)
            self.display_image(self.img)

    def display_image(self, img):
        if img is not None:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(img)
            img = ImageTk.PhotoImage(img)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=img)
            self.canvas.image = img

    def process_image(self):
        if self.img is not None:
            self.filtered_img = self.adjust_brightness(self.img, self.brightness)
            self.display_image(self.filtered_img)

    def adjust_brightness(self, img, alpha):
        # Điều chỉnh độ sáng bằng cách nhân từng giá trị pixel với alpha
        adjusted_img = cv2.convertScaleAbs(img, alpha=alpha*10, beta=2)
        return adjusted_img

    def update_brightness(self, value):
        self.brightness = float(value)  
        self.process_image()

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageProcessingApp(root)
    root.mainloop()
