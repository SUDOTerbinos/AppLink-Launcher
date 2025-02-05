import webbrowser
import os
import tkinter as tk
from PIL import Image, ImageTk

def open_link(url):
    """Opens the given URL in the web browser or app."""
    try:
        os.system(f"xdg-open {url}")  
    except:
        webbrowser.open(url)  

root = tk.Tk()
root.title("Open Apps & Websites")
root.geometry("400x500")

links = [
    ("YouTube", "https://www.youtube.com", "youtube.png"),
    ("Google", "https://www.google.com", "google.png"),
    ("Facebook", "https://www.facebook.com", "facebook.png"),
    ("Twitter", "https://twitter.com", "twitter.png"),
    ("Instagram", "https://www.instagram.com", "instagram.png"),
]

for name, url, img_path in links:
    image = Image.open(img_path)
    image = image.resize((80, 80))  
    photo = ImageTk.PhotoImage(image)

    btn = tk.Button(root, image=photo, command=lambda u=url: open_link(u), borderwidth=0)
    btn.image = photo  
    btn.pack(pady=10)


root.mainloop()
