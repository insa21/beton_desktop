import tkinter as tk
from tkinter import ttk, messagebox
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
        self.bg_image = None  # Store background image reference
        self.logo_image = None  # Store logo image reference
        self.setup_ui()

    def setup_ui(self):
        # Buat label untuk menampilkan gambar latar belakang
        try:
            background_image = Image.open("background.jpg")
            background_image = background_image.resize((1200, 800))
            self.bg_image = ImageTk.PhotoImage(background_image)

            background_label = tk.Label(self.root, image=self.bg_image)
            background_label.place(x=0, y=0, relwidth=1, relheight=1)
        except FileNotFoundError:
            print("Background image not found!")

        # Frame utama untuk komponen
        frame = ttk.Frame(self.root, padding="10")
        frame.place(relwidth=1, relheight=1)

        ttk.Label(frame, text="Pilih Mutu Beton:", font=("Helvetica", 12)).grid(row=0, column=0, pady=10, padx=10)
        self.mutu_var = tk.StringVar(value="K100")
        mutu_options = ["K100", "K150", "K225", "K250", "K275", "K300"]
        self.mutu_menu = ttk.Combobox(frame, textvariable=self.mutu_var, values=mutu_options, font=("Helvetica", 12))
        self.mutu_menu.grid(row=0, column=1, pady=10, padx=10)

        # Tambahkan logo
        try:
            logo_image = Image.open("logo.jpg")
            logo_image = logo_image.resize((100, 100))
            self.logo_image = ImageTk.PhotoImage(logo_image)

            logo_label = tk.Label(frame, image=self.logo_image)
            logo_label.grid(row=0, column=2, rowspan=2, pady=10, padx=10)
        except FileNotFoundError:
            print("Logo image not found!")

        kolom_frame = ttk.Frame(frame, padding="10")
        kolom_frame.grid(row=1, column=0, columnspan=2, sticky="ew")
        self.add_label(kolom_frame, "Dimensi dan Jumlah Kolom", 0)
        self.add_entry(kolom_frame, "Panjang Kolom (m):", "panjang_kolom", 1)
        self.add_entry(kolom_frame, "Lebar Kolom (m):", "lebar_kolom", 2)
        self.add_entry(kolom_frame, "Tinggi Kolom (m):", "tinggi_kolom", 3)
        self.add_entry(kolom_frame, "Jumlah Kolom:", "jumlah_kolom", 4)

        balok_frame = ttk.Frame(frame, padding="10")
        balok_frame.grid(row=1, column=2, columnspan=2, sticky="ew")
        self.add_label(balok_frame, "Dimensi dan Jumlah Balok", 0)
        self.add_entry(balok_frame, "Panjang Balok (m):", "panjang_balok", 1)
        self.add_entry(balok_frame, "Lebar Balok (m):", "lebar_balok", 2)
        self.add_entry(balok_frame, "Tinggi Balok (m):", "tinggi_balok", 3)
        self.add_entry(balok_frame, "Jumlah Balok:", "jumlah_balok", 4)

        plat_frame = ttk.Frame(frame, padding="10")
        plat_frame.grid(row=1, column=4, columnspan=2, sticky="ew")
        self.add_label(plat_frame, "Dimensi dan Jumlah Plat", 0)
        self.add_entry(plat_frame, "Panjang Plat (m):", "panjang_plat", 1)
        self.add_entry(plat_frame, "Lebar Plat (m):", "lebar_plat", 2)
        self.add_entry(plat_frame, "Tinggi Plat (m):", "tinggi_plat", 3)
        self.add_entry(plat_frame, "Jumlah Plat:", "jumlah_plat", 4)

        calculate_button = ttk.Button(frame, text="Hitung Kebutuhan Material", command=self.calculate)
        calculate_button.grid(row=2, columnspan=6, pady=20, padx=10)

    def add_label(self, parent, text, row):
        label = ttk.Label(parent, text=text, font=("Helvetica", 12))
        label.grid(row=row, column=0, columnspan=2, pady=5)

    def add_entry(self, parent, label_text, var_name, row):
        label = ttk.Label(parent, text=label_text, font=("Helvetica", 12))
        label.grid(row=row, column=0, padx=10, pady=5, sticky="e")
        entry = ttk.Entry(parent, font=("Helvetica", 12))
        entry.grid(row=row, column=1, padx=10, pady=5, sticky="w")
        setattr(self, var_name, entry)

    def calculate(self):
        try:
            panjang_kolom = float(self.panjang_kolom.get())
            lebar_kolom = float(self.lebar_kolom.get())
            tinggi_kolom = float(self.tinggi_kolom.get())
            jumlah_kolom = int(self.jumlah_kolom.get())

            panjang_balok = float(self.panjang_balok.get())
            lebar_balok = float(self.lebar_balok.get())
            tinggi_balok = float(self.tinggi_balok.get())
            jumlah_balok = int(self.jumlah_balok.get())

            panjang_plat = float(self.panjang_plat.get())
            lebar_plat = float(self.lebar_plat.get())
            tinggi_plat = float(self.tinggi_plat.get())
            jumlah_plat = int(self.jumlah_plat.get())

            total_volume_kolom = panjang_kolom * lebar_kolom * tinggi_kolom * jumlah_kolom
            total_volume_balok = panjang_balok * lebar_balok * tinggi_balok * jumlah_balok
            total_volume_plat = panjang_plat * lebar_plat * tinggi_plat * jumlah_plat

            total_volume = total_volume_kolom + total_volume_balok + total_volume_plat

            mutu = self.mutu_var.get()
            S = Beton[mutu]['Semen']
            P = Beton[mutu]['Pasir']
            K = Beton[mutu]['Kerikil']
            A = Beton[mutu]['Air']

            semen = total_volume * S
            pasir = total_volume * P
            kerikil = total_volume * K
            air = total_volume * A

            result = (
                f"Kebutuhan Semen: {round(semen)} kg\n"
                f"Kebutuhan Pasir: {round(pasir)} kg\n"
                f"Kebutuhan Kerikil: {round(kerikil)} kg\n"
                f"Kebutuhan Air: {round(air)} liter"
            )
            messagebox.showinfo("Hasil Perhitungan", result)
        except ValueError:
            messagebox.showerror("Error", "Input tidak valid. Pastikan semua nilai diisi dengan benar.")
        except KeyError:
            messagebox.showerror("Error", "Mutu beton tidak valid.")

if __name__ == '__main__':
    root = tk.Tk()
    app = BetonCalculatorApp(root)
    root.mainloop()
