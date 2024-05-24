import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime

class InvoicePage:
    def __init__(self, root, transaction):
        self.root = root
        self.transaction = transaction
        self.create_widgets()
    
    def create_widgets(self):
        # Clear previous content
        for widget in self.root.winfo_children():
            widget.destroy()

        # Title Label
        self.title_label = ctk.CTkLabel(self.root, text="Nota Transaksi", font=("Arial", 20))
        self.title_label.grid(row=0, columnspan=2, pady=10)

        # Transaction Details
        self.details_text = ctk.CTkTextbox(self.root, width=400, height=200, wrap='word', fg_color="black", text_color="white")
        self.details_text.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        transaction_details = (
            f"Jumlah Diamond: {self.transaction['amount']}\n"
            f"Harga: Rp {self.transaction['price']}\n"
            f"Penyedia Layanan: {self.transaction['provider']}\n"
            f"Email: {self.transaction['email']}\n"
            f"Status: {self.transaction['status']}\n"
            f"Tanggal: {self.transaction['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}\n"
        )
        self.details_text.insert("end", transaction_details)
        self.details_text.configure(state="disabled")

        # Download Invoice Button
        self.download_button = ctk.CTkButton(self.root, text="Unduh Nota", command=self.download_invoice)
        self.download_button.grid(row=2, column=0, pady=10)

        # Back Button
        self.back_button = ctk.CTkButton(self.root, text="Kembali", command=self.root.destroy)
        self.back_button.grid(row=2, column=1, pady=10)

    def download_invoice(self):
        invoice_content = (
            f"NOTA TRANSAKSI\n"
            f"====================\n"
            f"Jumlah Diamond: {self.transaction['amount']}\n"
            f"Harga: Rp {self.transaction['price']}\n"
            f"Penyedia Layanan: {self.transaction['provider']}\n"
            f"Email: {self.transaction['email']}\n"
            f"Status: {self.transaction['status']}\n"
            f"Tanggal: {self.transaction['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}\n"
        )
        file_name = f"invoice_{self.transaction['timestamp'].strftime('%Y%m%d_%H%M%S')}.txt"
        with open(file_name, "w") as file:
            file.write(invoice_content)
        
        messagebox.showinfo("Nota Disimpan", f"Nota transaksi telah disimpan sebagai {file_name}")
