# Day 36 — Using Pillow (PIL) to Display Images in Tkinter

Today I learned how to use the Pillow library to load, resize, and display images inside a Tkinter window. Pillow is a modern fork of PIL and is widely used for image processing tasks in Python.

---

## 🔍 What is Pillow?

Pillow (PIL) is a powerful library for:
- Opening images  
- Resizing images  
- Cropping  
- Format conversion  
- Drawing on images  
- Filters and enhancements  

It works perfectly with Tkinter when creating GUI applications involving images.

---

## 🚀 Steps Covered

### ✔ 1. Install Pillow  

### ✔ 2. Load an image using PIL  
### ✔ 3. Resize the image (optional)  
### ✔ 4. Convert PIL image → Tkinter image  
### ✔ 5. Display using `Label` widget  

---

## 🧩 Tkinter + Pillow Code

```python
import tkinter as tk
from PIL import Image, ImageTk

def main():
    root = tk.Tk()
    root.geometry("400x400")

    image_path = './download.jpg'
    
    pil_image = Image.open(image_path)
    pil_image = pil_image.resize((300, 300))
    tk_image = ImageTk.PhotoImage(pil_image)

    l1 = tk.Label(root, image=tk_image)
    l1.pack()

    root.mainloop()

if __name__ == '__main__':
    main()
🏁 Summary

Pillow makes image handling extremely easy, and when combined with Tkinter, it allows the creation of simple image viewers, galleries, and utility apps.
This was a great step toward more advanced GUI-based image tools.