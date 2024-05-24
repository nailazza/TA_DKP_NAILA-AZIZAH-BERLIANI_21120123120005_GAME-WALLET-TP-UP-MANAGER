import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime
import re

class PaymentPage:
    def __init__(self, root, app, index):
        self.root = root
        self.app = app
        self.index = index
        self.create_widgets()

    def create_widgets(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.root.title("Pembayaran")

        frame = ctk.CTkFrame(self.root)
        frame.place(relx=0.5, rely=0.5, anchor='center')

        transaction = self.app.current_user['history'][self.index]

        self.provider_label = ctk.CTkLabel(frame, text="Pilih Penyedia Layanan:")
        self.provider_label.grid(row=0, column=0, padx=10, pady=10)
        self.provider_var = ctk.StringVar()
        self.provider_combobox = ctk.CTkComboBox(frame, values=["GoPay", "ShopeePay", "Dana"], variable=self.provider_var)
        self.provider_combobox.grid(row=0, column=1, padx=10, pady=10)

        self.email_label = ctk.CTkLabel(frame, text="Masukkan Email:")
        self.email_label.grid(row=1, column=0, padx=10, pady=10)

        self.email_entry = ctk.CTkEntry(frame)
        self.email_entry.grid(row=1, column=1, padx=10, pady=10)

        self.price_label = ctk.CTkLabel(frame, text=f"Harga: Rp {transaction['price']}")
        self.price_label.grid(row=2, columnspan=2, pady=10)

        self.pay_button = ctk.CTkButton(frame, text="Bayar", command=self.pay_order)
        self.pay_button.grid(row=3, column=0, pady=10)

        self.cancel_button = ctk.CTkButton(frame, text="Batal", command=self.show_user_details_page)
        self.cancel_button.grid(row=3, column=1, pady=10)

    def pay_order(self):
        provider = self.provider_var.get()
        email = self.email_entry.get()
        if not provider or not email:
            messagebox.showerror("Input Error", "Harap isi semua data pembayaran.")
        elif not self.validate_email(email):
            messagebox.showerror("Input Error", "Format email tidak valid.")
        else:
            self.app.current_user['history'][self.index]['provider'] = provider
            self.app.current_user['history'][self.index]['email'] = email
            self.app.current_user['history'][self.index]['status'] = "Pesanan Berhasil"
            self.app.current_user['diamonds'] += self.app.current_user['history'][self.index]['amount']
            messagebox.showinfo("Pembayaran Berhasil", "Pesanan Anda telah dibayar.")
            self.show_user_details_page()

    def show_user_details_page(self):
        from UserDetailsPage import UserDetailsPage
        UserDetailsPage(self.root, self.app)

    def validate_email(self, email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email)


