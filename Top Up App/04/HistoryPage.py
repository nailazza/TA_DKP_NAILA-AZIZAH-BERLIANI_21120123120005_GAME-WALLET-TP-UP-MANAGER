import customtkinter as ctk
from tkinter import Text, messagebox
import tkinter as tk
from datetime import datetime

class HistoryPage:
    def __init__(self, root, app):
        self.root = root
        self.app = app
        self.create_widgets()

    def create_widgets(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.root.title("Riwayat Transaksi")

        frame = ctk.CTkFrame(self.root, fg_color="black")
        frame.place(relx=0.5, rely=0.5, anchor='center')

        self.history_text = Text(frame, width=50, height=20, wrap="word", bg="black", fg="white")
        self.history_text.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        history = self.app.current_user['history']
        for index, transaction in enumerate(history):
            transaction_text = (
                f"Top Up {transaction['amount']} Diamond "
                f"Harga: Rp {transaction['price']} "
                f"Status: {transaction['status']} "
                f"Tanggal: {transaction['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}\n"
            )
            self.history_text.insert("end", transaction_text)

            if transaction['status'] == "Belum Bayar":
                pay_button = ctk.CTkButton(frame, text="Bayar Pesanan", command=lambda idx=index: self.show_payment_page(idx))
                self.history_text.window_create("end", window=pay_button)
                self.history_text.insert("end", " ")  # Add space between buttons
                cancel_button = ctk.CTkButton(frame, text="Batalkan Pesanan", command=lambda idx=index: self.cancel_order(idx))
                self.history_text.window_create("end", window=cancel_button)
            elif transaction['status'] == "Pesanan Berhasil":
                invoice_button = ctk.CTkButton(frame, text="Lihat Nota", command=lambda idx=index: self.show_invoice(idx))
                self.history_text.window_create("end", window=invoice_button)
            self.history_text.insert("end", "\n\n")

        self.history_text.configure(state="disabled")

        self.back_button = ctk.CTkButton(frame, text="Kembali", command=self.show_user_details_page)
        self.back_button.grid(row=1, columnspan=2, pady=10)

    def cancel_order(self, index):
        self.app.current_user['history'][index]['status'] = "Pesanan Dibatalkan"
        messagebox.showinfo("Pesanan Dibatalkan", "Pesanan berhasil dibatalkan.")
        self.create_widgets()

    def show_payment_page(self, index):
        from PaymentPage import PaymentPage
        PaymentPage(self.root, self.app, index)

    def show_invoice(self, index):
        from InvoicePage import InvoicePage
        transaction = self.app.current_user['history'][index]
        InvoicePage(ctk.CTkToplevel(self.root), transaction)

    def show_user_details_page(self):
        from UserDetailsPage import UserDetailsPage
        UserDetailsPage(self.root, self.app)
