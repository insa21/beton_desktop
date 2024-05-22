import tkinter as tk
from tkinter import ttk, messagebox
from ttkbootstrap import Style

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

        # Menggunakan tema yang ada di ttkbootstrap
        self.style = Style(theme="solar")
        self.root.geometry("400x790")

        self.setup_ui()

    def setup_ui(self):
        frame = ttk.Frame(self.root, padding="10")
        frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(frame, text="Pilih Mutu Beton:", font=("Helvetica", 12)).grid(row=0, column=0, pady=10, padx=10)
        self.mutu_var = tk.StringVar(value="K100")
        mutu_options = ["K100", "K150", "K225", "K250", "K275", "K300"]
        self.mutu_menu = ttk.Combobox(frame, textvariable=self.mutu_var, values=mutu_options, font=("Helvetica", 12))
        self.mutu_menu.grid(row=0, column=1, pady=10, padx=10)

        self.add_label(frame, "Dimensi dan Jumlah Kolom", 1)
        self.add_entry(frame, "Panjang Kolom (m):", 2)
        self.add_entry(frame, "Lebar Kolom (m):", 3)
        self.add_entry(frame, "Tinggi Kolom (m):", 4)
        self.add_entry(frame, "Jumlah Kolom:", 5)

        self.add_label(frame, "Dimensi dan Jumlah Balok", 6)
        self.add_entry(frame, "Panjang Balok (m):", 7)
        self.add_entry(frame, "Lebar Balok (m):", 8)
        self.add_entry(frame, "Tinggi Balok (m):", 9)
        self.add_entry(frame, "Jumlah Balok:", 10)

        self.add_label(frame, "Dimensi dan Jumlah Plat", 11)
        self.add_entry(frame, "Panjang Plat (m):", 12)
        self.add_entry(frame, "Lebar Plat (m):", 13)
        self.add_entry(frame, "Tinggi Plat (m):", 14)
        self.add_entry(frame, "Jumlah Plat:", 15)

        calculate_button = ttk.Button(frame, text="Hitung Kebutuhan Material", command=self.calculate, style="primary.TButton")
        calculate_button.grid(row=16, columnspan=2, pady=20, padx=10)

    def add_label(self, frame, label_text, row):
        ttk.Label(frame, text=label_text, font=("Helvetica", 14, "bold")).grid(row=row, columnspan=2, pady=10, padx=10)

    def add_entry(self, frame, label_text, row):
        ttk.Label(frame, text=label_text, font=("Helvetica", 12)).grid(row=row, column=0, pady=5, padx=10)
        entry = ttk.Entry(frame, font=("Helvetica", 12))
        entry.grid(row=row, column=1, pady=5, padx=10)
        setattr(self, f"entry_{row}", entry)

    def calculate(self):
        try:
            panjang_kolom = float(self.entry_2.get())
            lebar_kolom = float(self.entry_3.get())
            tinggi_kolom = float(self.entry_4.get())
            jumlah_kolom = int(self.entry_5.get())

            panjang_balok = float(self.entry_7.get())
            lebar_balok = float(self.entry_8.get())
            tinggi_balok = float(self.entry_9.get())
            jumlah_balok = int(self.entry_10.get())

            panjang_plat = float(self.entry_12.get())
            lebar_plat = float(self.entry_13.get())
            tinggi_plat = float(self.entry_14.get())
            jumlah_plat = int(self.entry_15.get())

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

if __name__ == '__main__':
    root = tk.Tk()
    app = BetonCalculatorApp(root)
    root.mainloop()
