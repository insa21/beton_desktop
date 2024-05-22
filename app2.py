import tkinter as tk
from tkinter import ttk, messagebox

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
        self.root.title("Hitung Kebutuhan Material Beton")
        
        self.create_widgets()

    def create_widgets(self):
        # Mutu Beton
        self.label_mutu = ttk.Label(self.root, text="Pilih Mutu Beton:")
        self.label_mutu.grid(column=0, row=0, padx=10, pady=5)

        self.combo_mutu = ttk.Combobox(self.root, values=list(Beton.keys()))
        self.combo_mutu.grid(column=1, row=0, padx=10, pady=5)
        self.combo_mutu.current(0)

        # Rasio Beton
        self.label_rasio = ttk.Label(self.root, text="Pilih Rasio Beton:")
        self.label_rasio.grid(column=0, row=1, padx=10, pady=5)

        self.combo_rasio = ttk.Combobox(self.root, values=["1:2:3", "1:2:4"])
        self.combo_rasio.grid(column=1, row=1, padx=10, pady=5)
        self.combo_rasio.current(0)

        # Dimensi Kolom
        self.label_dimensi_kolom = ttk.Label(self.root, text="Dimensi Kolom")
        self.label_dimensi_kolom.grid(column=0, row=2, columnspan=2, padx=10, pady=10)

        self.label_pA = ttk.Label(self.root, text="Panjang Kolom (m):")
        self.label_pA.grid(column=0, row=3, padx=10, pady=5)
        self.entry_pA = ttk.Entry(self.root)
        self.entry_pA.grid(column=1, row=3, padx=10, pady=5)

        self.label_lA = ttk.Label(self.root, text="Lebar Kolom (m):")
        self.label_lA.grid(column=0, row=4, padx=10, pady=5)
        self.entry_lA = ttk.Entry(self.root)
        self.entry_lA.grid(column=1, row=4, padx=10, pady=5)

        self.label_tA = ttk.Label(self.root, text="Tinggi Kolom (m):")
        self.label_tA.grid(column=0, row=5, padx=10, pady=5)
        self.entry_tA = ttk.Entry(self.root)
        self.entry_tA.grid(column=1, row=5, padx=10, pady=5)

        self.label_NA = ttk.Label(self.root, text="Jumlah Kolom:")
        self.label_NA.grid(column=0, row=6, padx=10, pady=5)
        self.entry_NA = ttk.Entry(self.root)
        self.entry_NA.grid(column=1, row=6, padx=10, pady=5)

        # Dimensi Balok
        self.label_dimensi_balok = ttk.Label(self.root, text="Dimensi Balok")
        self.label_dimensi_balok.grid(column=0, row=7, columnspan=2, padx=10, pady=10)

        self.label_pB = ttk.Label(self.root, text="Panjang Balok (m):")
        self.label_pB.grid(column=0, row=8, padx=10, pady=5)
        self.entry_pB = ttk.Entry(self.root)
        self.entry_pB.grid(column=1, row=8, padx=10, pady=5)

        self.label_lB = ttk.Label(self.root, text="Lebar Balok (m):")
        self.label_lB.grid(column=0, row=9, padx=10, pady=5)
        self.entry_lB = ttk.Entry(self.root)
        self.entry_lB.grid(column=1, row=9, padx=10, pady=5)

        self.label_tB = ttk.Label(self.root, text="Tinggi Balok (m):")
        self.label_tB.grid(column=0, row=10, padx=10, pady=5)
        self.entry_tB = ttk.Entry(self.root)
        self.entry_tB.grid(column=1, row=10, padx=10, pady=5)

        self.label_NB = ttk.Label(self.root, text="Jumlah Balok:")
        self.label_NB.grid(column=0, row=11, padx=10, pady=5)
        self.entry_NB = ttk.Entry(self.root)
        self.entry_NB.grid(column=1, row=11, padx=10, pady=5)

        # Dimensi Plat
        self.label_dimensi_plat = ttk.Label(self.root, text="Dimensi Plat")
        self.label_dimensi_plat.grid(column=0, row=12, columnspan=2, padx=10, pady=10)

        self.label_pP = ttk.Label(self.root, text="Panjang Plat (m):")
        self.label_pP.grid(column=0, row=13, padx=10, pady=5)
        self.entry_pP = ttk.Entry(self.root)
        self.entry_pP.grid(column=1, row=13, padx=10, pady=5)

        self.label_lP = ttk.Label(self.root, text="Lebar Plat (m):")
        self.label_lP.grid(column=0, row=14, padx=10, pady=5)
        self.entry_lP = ttk.Entry(self.root)
        self.entry_lP.grid(column=1, row=14, padx=10, pady=5)

        self.label_tP = ttk.Label(self.root, text="Tinggi Plat (m):")
        self.label_tP.grid(column=0, row=15, padx=10, pady=5)
        self.entry_tP = ttk.Entry(self.root)
        self.entry_tP.grid(column=1, row=15, padx=10, pady=5)

        self.label_NP = ttk.Label(self.root, text="Jumlah Plat:")
        self.label_NP.grid(column=0, row=16, padx=10, pady=5)
        self.entry_NP = ttk.Entry(self.root)
        self.entry_NP.grid(column=1, row=16, padx=10, pady=5)

        # Tombol hitung
        self.button_calculate = ttk.Button(self.root, text="Hitung Kebutuhan Material", command=self.calculate)
        self.button_calculate.grid(column=0, row=17, columnspan=2, padx=10, pady=20)

    def calculate(self):
        try:
            mutuBeton = self.combo_mutu.get()
            rasio = self.combo_rasio.get()

            pA = float(self.entry_pA.get())
            lA = float(self.entry_lA.get())
            tA = float(self.entry_tA.get())
            NA = float(self.entry_NA.get())
            volA = pA * lA * tA * NA

            pB = float(self.entry_pB.get())
            lB = float(self.entry_lB.get())
            tB = float(self.entry_tB.get())
            NB = float(self.entry_NB.get())
            volB = pB * lB * tB * NB

            pP = float(self.entry_pP.get())
            lP = float(self.entry_lP.get())
            tP = float(self.entry_tP.get())
            NP = float(self.entry_NP.get())
            volP = pP * lP * tP * NP

            totalVolume = volA + volB + volP

            S = Beton[mutuBeton]['Semen']
            K = Beton[mutuBeton]['Pasir']
            P = Beton[mutuBeton]['Kerikil']
            A = Beton[mutuBeton]['Air']

            if rasio == "1:2:3":
                semen = totalVolume * S * 1/6
                pasir = totalVolume * S * 2/6
                kerikil = totalVolume * S * 3/6
                air = totalVolume * A
            elif rasio == "1:2:4":
                semen = totalVolume * S * 1/7
                pasir = totalVolume * S * 2/7
                kerikil = totalVolume * S * 4/7
                air = totalVolume * A

            messagebox.showinfo("Hasil Perhitungan", f"Semen: {round(semen)} kg\nPasir: {round(pasir)} kg\nKerikil: {round(kerikil)} kg\nAir: {round(air)} liter")
        except ValueError:
            messagebox.showerror("Error", "Input tidak valid. Pastikan semua nilai diisi dengan benar.")

if __name__ == '__main__':
    root = tk.Tk()
    app = BetonCalculatorApp(root)
    root.mainloop()
