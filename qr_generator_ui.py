import tkinter as tk
from tkinter import filedialog, messagebox
import qrcode
from PIL import Image, ImageTk
import os

class QRGenerator:
    def __init__(self, master):
        self.master = master
        master.title("QR Code Generator")

        self.qr_image = None

        # Add the centered text in purple
        title_label = tk.Label(master, text="QR Generator created by Ashwin Reddy - Kairos", 
                               font=("Arial", 12, "bold"), fg="purple")
        title_label.pack(pady=10)

        tk.Label(master, text="Enter data for QR code:").pack(pady=10)
        self.entry = tk.Entry(master, width=50)
        self.entry.pack(pady=10)

        generate_button = tk.Button(master, text="Generate QR Code", command=self.generate_qr)
        generate_button.pack(pady=10)

        self.qr_label = tk.Label(master)
        self.qr_label.pack(pady=10)

        save_button = tk.Button(master, text="Save QR Code", command=self.save_qr)
        save_button.pack(pady=10)

    def generate_qr(self):
        data = self.entry.get()
        if not data:
            messagebox.showerror("Error", "Please enter data for the QR code")
            return
        
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(data)
        qr.make(fit=True)
        
        self.qr_image = qr.make_image(fill_color="black", back_color="white")
        
        # Display the QR code
        photo = ImageTk.PhotoImage(self.qr_image)
        self.qr_label.config(image=photo)
        self.qr_label.image = photo

    def save_qr(self):
        if self.qr_image is None:
            messagebox.showerror("Error", "Please generate a QR code first")
            return
        
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            self.qr_image.save(file_path)
            messagebox.showinfo("Success", f"QR code saved as {file_path}")

root = tk.Tk()
qr_generator = QRGenerator(root)
root.mainloop()
