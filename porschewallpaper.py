import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from io import BytesIO
import requests
import os
from datetime import datetime
from tkinter import messagebox

def show_image():
    global photo, original_img
    url = "https://source.unsplash.com/random/1920x1080?porsche+930"
    response = requests.get(url)
    original_img = Image.open(BytesIO(response.content))
    img = original_img.resize((600, 400))
    photo = ImageTk.PhotoImage(img)
    label.config(image=photo)
    label.image = photo

def save_image():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"porsche_930_{timestamp}.jpg"
    path = os.path.expanduser(f"~/Desktop/{filename}")
    response = messagebox.askyesno("Save Image", "Do you want to save this image to your desktop in Full Resolution?")
    if response == True:
        original_img.save(path)
        messagebox.showinfo("Saved", f"Image saved to desktop as {filename}!")
    else:
        messagebox.showinfo("Not Saved", "Image not saved.")

root = tk.Tk()
root.title("Porsche 930")

button1 = ttk.Button(root, text="Show Random Image", command=lambda: show_image())
button1.pack()

label = ttk.Label(root)
label.pack()

save_button = ttk.Button(root, text="Save Image", command=lambda: save_image())
save_button.pack()

root.mainloop()
