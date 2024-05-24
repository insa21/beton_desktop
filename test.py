import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


def create_app():
    root = tk.Tk()
    root.title("Desktop Application with Background Image")
    root.geometry("800x600")

    try:
        # Load background image
        with Image.open("background.jpg") as bg_image:
            bg_image.thumbnail((1200, 600))  # Resize with anti-aliasing
            bg_photo = ImageTk.PhotoImage(bg_image)

        # Create label for background
        bg_label = tk.Label(root, image=bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    except FileNotFoundError:
        print("Background image not found!")

    # Create frame for form on top of background
    form_frame = tk.Frame(root, bg='white', bd=2, relief=tk.RAISED)
    form_frame.place(relx=0.5, rely=0.5, anchor='center', width=400, height=300)

    try:
        # Load logo image
        with Image.open("logo.jpg") as logo_image:
            logo_image.thumbnail((100, 100))  # Resize with anti-aliasing
            logo_photo = ImageTk.PhotoImage(logo_image)

        # Add logo
        logo_label = tk.Label(form_frame, image=logo_photo, bg='white')
        logo_label.pack(pady=10)
    except FileNotFoundError:
        print("Logo image not found!")

    # Add fields to the form
    labels = ["Kriteria 1", "Kriteria 2", "Kriteria 3"]
    entries = []
    for label_text in labels:
        tk.Label(form_frame, text=label_text, bg='white').pack(pady=5)
        entry = ttk.Entry(form_frame)
        entry.pack(pady=5)
        entries.append(entry)

    # Add submit button
    submit_button = ttk.Button(form_frame, text="Submit")
    submit_button.pack(pady=20)

    root.mainloop()


create_app()
