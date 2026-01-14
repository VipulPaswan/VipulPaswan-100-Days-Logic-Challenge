import tkinter as tk
from PIL import Image,ImageTk

def main():
    root = tk.Tk()
    root.geometry("400x400")
    image_path='./download.jpg'
    pil_image = Image.open(image_path)
    pil_image = pil_image.resize((300,300)) 
    tk_image = ImageTk.PhotoImage(pil_image)

    l1=tk.Label(root,image=tk_image)
    l1.pack()

    root.mainloop()
       
if __name__=='__main__':
    main()
    
    