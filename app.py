import tkinter as tk
from tkinter import ttk, messagebox
from ttkbootstrap import Style
from PIL import Image, ImageTk

# Data untuk berbagai mutu beton
Beton = {
    'K100': {'Semen': 247, 'Pasir': 869, 'Kerikil': 869, 'Air': 215, 'w/c': 0.87},
    'K150': {'Semen': 299, 'Pasir': 799, 'Kerikil': 1017, 'Air': 215, 'w/c': 0.72},
    'K225': {'Semen': 371, 'Pasir': 698, 'Kerikil': 1047, 'Air': 215, 'w/c': 0.58},
    'K250': {'Semen': 384, 'Pasir': 692, 'Kerikil': 1039, 'Air': 215, 'w/c': 0.56},
    'K275': {'Semen': 384, 'Pasir': 692, 'Kerikil': 1039, 'Air': 215, 'w/c': 0.56},
    'K300': {'Semen': 384, 'Pasir': 692, 'Kerikil': 1039, 'Air': 215, 'w/c': 0.56}
}

class BetonCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Beton Calculator")
        self.root.geometry("1200x800")

        self.labels = [
            "Panjang Kolom (m):", "Lebar Kolom (m):", "Tinggi Kolom (m):", "Jumlah Kolom:",
            "Panjang Balok (m):", "Lebar Balok (m):", "Tinggi Balok (m):", "Jumlah Balok:",
            "Panjang Plat (m):", "Lebar Plat (m):", "Tinggi Plat (m):", "Jumlah Plat:"
        ]

        self.setup_ui()

    def setup_ui(self):
        try:
            # Load background image
            with Image.open("background.jpg") as bg_image:
                bg_image = bg_image.resize((1490, 890))  # Resize with anti-aliasing
                self.bg_photo = ImageTk.PhotoImage(bg_image)

            # Create label for background
            bg_label = tk.Label(self.root, image=self.bg_photo)
            bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        except FileNotFoundError:
            print("Background image not found!")

        # Create frame for form on top of background
        form_frame = tk.Frame(self.root, bg='white', bd=2, relief=tk.RAISED)
        form_frame.place(relx=0.5, rely=0.5, anchor='center', width=1000, height=600)

        try:
            # Load logo image
            with Image.open("logo.jpg") as logo_image:
                logo_image.thumbnail((120, 120))  # Resize with anti-aliasing
                self.logo_photo = ImageTk.PhotoImage(logo_image)

            # Add logo
            logo_label = tk.Label(form_frame, image=self.logo_photo, bg='white')
            logo_label.pack(pady=10)
        except FileNotFoundError:
            print("Logo image not found!")

        # Add fields to the form
        ttk.Label(form_frame, text="Pilih Mutu Beton:", font=("Helvetica", 12), background='white').pack(pady=5)
        self.mutu_var = tk.StringVar(value="K100")
        mutu_options = ["K100", "K150", "K225", "K250", "K275", "K300"]
        self.mutu_menu = ttk.Combobox(form_frame, textvariable=self.mutu_var, values=mutu_options, font=("Helvetica", 12))
        self.mutu_menu.pack(pady=5)

        self.entry_frame = tk.Frame(form_frame, bg='white')
        self.entry_frame.pack(pady=10)

        self.entries = {}

        # Divide labels into three columns
        num_labels = len(self.labels)
        num_columns = 3
        labels_per_column = num_labels // num_columns

        for col in range(num_columns):
            for i in range(col * labels_per_column, (col + 1) * labels_per_column):
                label_text = self.labels[i]
                label = ttk.Label(self.entry_frame, text=label_text, font=("Helvetica", 12), background='white')
                label.grid(row=i % labels_per_column, column=col * 2, pady=2)
                entry = ttk.Entry(self.entry_frame, font=("Helvetica", 12))
                entry.grid(row=i % labels_per_column, column=col * 2 + 1, pady=2)
                self.entries[label_text] = entry

        calculate_button = ttk.Button(form_frame, text="Hitung Kebutuhan Material", command=self.calculate)
        calculate_button.pack(pady=20)

        # Create a treeview widget for the table
        self.tree = ttk.Treeview(form_frame, columns=("Material", "Kebutuhan"), show="headings")
        self.tree.heading("Material", text="Material", anchor=tk.CENTER)
        self.tree.heading("Kebutuhan", text="Kebutuhan", anchor=tk.CENTER)
        self.tree.column("Material", anchor=tk.CENTER)
        self.tree.column("Kebutuhan", anchor=tk.CENTER)
        self.tree.pack(pady=10, expand=True, fill="both")

    def calculate(self):
        try:
            # Collect input values
            kolom_values = [float(self.entries[label].get()) for label in self.labels[:4]]
            balok_values = [float(self.entries[label].get()) for label in self.labels[4:8]]
            plat_values = [float(self.entries[label].get()) for label in self.labels[8:]]

            # Calculate total volumes
            total_volume_kolom = kolom_values[0] * kolom_values[1] * kolom_values[2] * kolom_values[3]
            total_volume_balok = balok_values[0] * balok_values[1] * balok_values[2] * balok_values[3]
            total_volume_plat = plat_values[0] * plat_values[1] * plat_values[2] * plat_values[3]

            # Calculate total volume
            total_volume = total_volume_kolom + total_volume_balok + total_volume_plat

            # Get material ratios
            mutu = self.mutu_var.get()
            S, P, K, A = Beton[mutu]['Semen'], Beton[mutu]['Pasir'], Beton[mutu]['Kerikil'], Beton[mutu]['Air']

            # Calculate material needs
            semen = total_volume * S
            pasir = total_volume * P
            kerikil = total_volume * K
            air = total_volume * A

            # Clear existing rows in the treeview
            for row in self.tree.get_children():
                self.tree.delete(row)

            # Insert rows for each material
            self.tree.insert("", "end", values=("Semen", round(semen, 2)))
            self.tree.insert("", "end", values=("Pasir", round(pasir, 2)))
            self.tree.insert("", "end", values=("Kerikil", round(kerikil, 2)))
            self.tree.insert("", "end", values=("Air", round(air, 2)))

        except ValueError:
            messagebox.showerror("Error", "Input tidak valid. Pastikan semua nilai diisi dengan benar.")
        except KeyError:
            messagebox.showerror("Error", "Mutu beton tidak valid.")


if __name__ == '__main__':
    root = tk.Tk()
    app = BetonCalculatorApp(root)
    root.mainloop()
