import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image
import main

def select_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        output_path = main.detect_faces(file_path)
        show_image(output_path)

def show_image(image_path):
    image = Image.open(image_path)
    image = image.resize((400, 400), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)

    panel.configure(image=image)
    panel.image = image

app = tk.Tk()
app.title("Face Detection using Haarcascade")

select_button = tk.Button(app, text="Select Image", command=select_image)
select_button.pack(side="top", fill="both", expand="yes", padx="10", pady="10")

panel = tk.Label(app)
panel.pack(side="bottom", fill="both", expand="yes")

app.mainloop()