import tkinter as tk
from tkinter import messagebox

def hitung_molaritas():
    try:
        mol=float(entry_mol.get())
        volume=float(entry_volume.get())
        hasil=mol/volume
        messagebox.showinfo("Hasil",f"Molaritas = {hasil:.4f},M")
    except ValueError:
         messagebox.showerror("Error","Input tidak valid!")

def hitung_normalitas():
    try:
        mol = float(entry_mol.get())
        volume = float(entry_volume.get())
        valensi = int(entry_valensi.get())
        hasil = (mol * valensi) / volume
        messagebox.showinfo("Hasil", f"Normalitas = {hasil:.4f} N")
    except ValueError:
        messagebox.showerror("Error", "Input tidak valid!")

def hitung_molalitas():
    try:
        mol = float(entry_mol.get())
        massa_pelarut = float(entry_massa_pelarut.get())
        hasil = mol / massa_pelarut
        messagebox.showinfo("Hasil", f"Molalitas = {hasil:.4f} m")
    except ValueError:
        messagebox.showerror("Error", "Input tidak valid!")

def hitung_ppm():
    try:
        massa_zat = float(entry_massa_zat.get())
        volume = float(entry_volume.get())
        hasil = massa_zat / volume
        messagebox.showinfo("Hasil",f"PPM = {hasil:.2f},ppm")
    except ValueError:
        messagebox.showerror("Error","Input tidak valid!")


# GUI setup
root = tk.Tk()
root.title("Kalkulator Konsentrasi Kimia")


# Label dan Entry untuk input
tk.Label(root, text="Jumlah Mol (mol):").grid(row=0, column=0)
entry_mol = tk.Entry(root)
entry_mol.grid(row=0, column=1)

tk.Label(root, text="Volume Larutan (L):").grid(row=1, column=0)
entry_volume = tk.Entry(root)
entry_volume.grid(row=1, column=1)

tk.Label(root, text="Massa Pelarut (kg):").grid(row=2, column=0)
entry_massa_pelarut = tk.Entry(root)
entry_massa_pelarut.grid(row=2, column=1)

tk.Label(root, text="Valensi:").grid(row=3, column=0)
entry_valensi = tk.Entry(root)
entry_valensi.grid(row=3, column=1)

tk.Label(root, text="Massa Zat (mg):").grid(row=4, column=0)
entry_massa_zat = tk.Entry(root)
entry_massa_zat.grid(row=4, column=1)

tk.Button(root, text="Hitung Molaritas", command=hitung_molaritas).grid(row=5, column=0, pady=5)
tk.Button(root, text="Hitung Normalitas", command=hitung_normalitas).grid(row=5, column=1, pady=5)
tk.Button(root, text="Hitung Molalitas", command=hitung_molalitas).grid(row=6, column=0, pady=5)
tk.Button(root, text="Hitung PPM", command=hitung_ppm).grid(row=6, column=1, pady=5)

root.mainloop()
