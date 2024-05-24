import customtkinter as ctk

class UserDetailsPage:
    def __init__(self, root, app):
        self.root = root
        self.app = app
        self.create_widgets()

    def create_widgets(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.root.title("Detail Pengguna")

        frame = ctk.CTkFrame(self.root)
        frame.place(relx=0.5, rely=0.5, anchor='center')

        self.username_label = ctk.CTkLabel(frame, text=f"Username: {self.app.current_user['username']}")
        self.username_label.grid(row=0, columnspan=2, padx=10, pady=10)

        self.diamonds_label = ctk.CTkLabel(frame, text=f"Jumlah Diamond: {self.app.current_user['diamonds']}")
        self.diamonds_label.grid(row=1, columnspan=2, padx=10, pady=10)

        self.topup_button = ctk.CTkButton(frame, text="Top Up Diamond", command=self.show_topup_page)
        self.topup_button.grid(row=2, column=0, pady=10, padx=10)

        self.history_button = ctk.CTkButton(frame, text="Lihat Riwayat Transaksi", command=self.show_history_page)
        self.history_button.grid(row=2, column=1, pady=10, padx=10)

        self.back_button = ctk.CTkButton(frame, text="Kembali", command=self.show_initial_page)
        self.back_button.grid(row=3, columnspan=2, pady=10)

    def show_topup_page(self):
        from TopUpPage import TopUpPage
        TopUpPage(self.root, self.app)

    def show_history_page(self):
        from HistoryPage import HistoryPage
        HistoryPage(self.root, self.app)

    def show_initial_page(self):
        from InitialPage import InitialPage
        InitialPage(self.root, self.app)
