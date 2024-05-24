import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime

class TopUpPage:
    def __init__(self, root, app):
        self.root = root
        self.app = app
        self.price_list = {
            "3": 1171,
            "5": 1423,
            "12": 3323,
            "19": 5223,
            "28": 7600,
            "44": 11400
        }
        self.create_widgets()

    def create_widgets(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.root.title("Top Up Diamond")

        frame = ctk.CTkFrame(self.root)
        frame.place(relx=0.5, rely=0.5, anchor='center')

        self.amount_label = ctk.CTkLabel(frame, text="Jumlah Diamond:")
        self.amount_label.grid(row=0, column=0, padx=10, pady=10)

        self.amount_var = ctk.StringVar()
        self.amount_combobox = ctk.CTkComboBox(frame, values=["3", "5", "12", "19", "28", "44"], variable=self.amount_var)
        self.amount_combobox.grid(row=0, column=1, padx=10, pady=10)

        self.price_label = ctk.CTkLabel(frame, text="Harga Diamond:")
        self.price_label.grid(row=1, column=0, padx=10, pady=10)

        self.price_text = ctk.CTkTextbox(frame, height=100, width=200)
        self.price_text.grid(row=2, columnspan=2, padx=10, pady=10)
        self.price_text.insert("0.0", "\n".join([f"{k} diamonds = Rp {v}" for k, v in self.price_list.items()]))
        self.price_text.configure(state="disabled")

        self.create_order_button = ctk.CTkButton(frame, text="Buat Pesanan", command=self.create_order)
        self.create_order_button.grid(row=3, column=0, pady=10, padx=10)

        self.back_button = ctk.CTkButton(frame, text="Kembali", command=self.show_user_details_page)
        self.back_button.grid(row=3, column=1, pady=10, padx=10)

    def create_order(self):
        amount = self.amount_var.get()
        if not amount:
            messagebox.showerror("Input Error", "Harap pilih jumlah diamond.")
        else:
            price = self.price_list[amount]
            transaction = {
                "amount": int(amount),
                "price": price,
                "provider": None,
                "email": None,
                "status": "Belum Bayar",
                "timestamp": datetime.now()
            }
            self.app.current_user['history'].append(transaction)
            self.show_payment_page(len(self.app.current_user['history']) - 1)

    def show_user_details_page(self):
        from UserDetailsPage import UserDetailsPage
        UserDetailsPage(self.root, self.app)

    def show_payment_page(self, index):
        from PaymentPage import PaymentPage
        PaymentPage(self.root, self.app, index)
