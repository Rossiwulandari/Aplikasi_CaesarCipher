import tkinter as tk
from tkinter import messagebox

# Fungsi enkripsi menggunakan Caesar Cipher
def enkripsi(plaint_text, shift):
    cipher_text = ""
    for char in plaint_text:
        # Huruf besar
        if char.isupper():
            cipher_text += chr((ord(char) + shift - 65) % 26 + 65)
        # Huruf kecil
        elif char.islower():
            cipher_text += chr((ord(char) + shift - 97) % 26 + 97)
        # Karakter selain huruf
        else:
            cipher_text += char
    return cipher_text

# Fungsi dekripsi menggunakan Caesar Cipher
def dekripsi(cipher_text, shift):
    plaint_text = ""
    for char in cipher_text:
        # Huruf besar
        if char.isupper():
            plaint_text += chr((ord(char) - shift - 65) % 26 + 65)
        # Huruf kecil
        elif char.islower():
            plaint_text += chr((ord(char) - shift - 97) % 26 + 97)
        # Karakter selain huruf
        else:
            plaint_text += char
    return plaint_text

# Fungsi untuk menangani aksi enkripsi dan dekripsi
def proses_enkripsi_dekripsi():
    plaint_text = entry_plaintext.get()  # Ambil teks dari input
    try:
        shift = int(entry_shift.get())  # Ambil nilai pergeseran
        if not (1 <= shift <= 25):
            raise ValueError("Shift harus antara 1 dan 25.")
        
        # Panggil fungsi enkripsi
        cipher_text = enkripsi(plaint_text, shift)
        label_ciphertext.config(text=f"Teks Enkripsi: {cipher_text}")
        
        # Panggil fungsi dekripsi
        decrypted_text = dekripsi(cipher_text, shift)
        label_decryptedtext.config(text=f"Teks Dekripsi: {decrypted_text}")
    
    except ValueError as e:
        messagebox.showerror("Input Error", f"Terjadi kesalahan: {str(e)}")

# Membuat jendela utama dengan Tkinter
root = tk.Tk()
root.title("Aplikasi Caesar Cipher")

root.geometry("600x500")  # Ukuran jendela
root.config(bg="#D2B48C")  # Warna latar belakang coklat susu

# Label untuk teks asli
label_plaintext = tk.Label(root, text="Masukkan Teks Asli (Plaintext):", font=("Arial", 14), bg="#D2B48C", anchor='w')
label_plaintext.pack(pady=10)

# Entry untuk memasukkan teks asli
entry_plaintext = tk.Entry(root, width=60, font=("Arial", 14), bg="#FFF5EE", bd=2)
entry_plaintext.pack(pady=10)

# Label untuk pergeseran
label_shift = tk.Label(root, text="Masukkan Nilai Pergeseran (1-25):", font=("Arial", 14), bg="#D2B48C", anchor='w')
label_shift.pack(pady=10)

# Entry untuk memasukkan nilai pergeseran
entry_shift = tk.Entry(root, width=60, font=("Arial", 14), bg="#FFF5EE", bd=2)
entry_shift.pack(pady=10)

# Tombol untuk memproses enkripsi dan dekripsi
button_proses = tk.Button(root, text="Proses Enkripsi dan Dekripsi", command=proses_enkripsi_dekripsi, 
                          font=("Arial", 14, "bold"), bg="#D2B48C", fg="black", bd=2)
button_proses.pack(pady=20)

# Label untuk menampilkan hasil enkripsi
label_ciphertext = tk.Label(root, text="Teks Enkripsi: ", font=("Arial", 14), bg="#D2B48C", anchor='w')
label_ciphertext.pack(pady=10)

# Label untuk menampilkan hasil dekripsi
label_decryptedtext = tk.Label(root, text="Teks Dekripsi: ", font=("Arial", 14), bg="#D2B48C", anchor='w')
label_decryptedtext.pack(pady=10)

# Menjalankan GUI
root.mainloop()