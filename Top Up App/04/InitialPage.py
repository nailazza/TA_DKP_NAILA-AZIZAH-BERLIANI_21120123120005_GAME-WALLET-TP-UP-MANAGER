import customtkinter as ctk
from tkinter import messagebox

class InitialPage:
    def __init__(self, root, app):
        self.root = root
        self.app = app
        self.create_widgets()

    def create_widgets(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.root.title("Cari Pengguna")
        
        frame = ctk.CTkFrame(self.root)
        frame.place(relx=0.5, rely=0.5, anchor='center')

        self.id_label = ctk.CTkLabel(frame, text="Masukkan ID Pengguna:")
        self.id_label.grid(row=0, column=0, padx=10, pady=10)

        self.id_entry = ctk.CTkEntry(frame)
        self.id_entry.grid(row=0, column=1, padx=10, pady=10)

        self.search_button = ctk.CTkButton(frame, text="Cari", command=self.search_user)
        self.search_button.grid(row=1, columnspan=2, pady=10)

        self.root.bind('<Return>', lambda event=None: self.search_button.invoke())

    def search_user(self):
        user_id = self.id_entry.get()
        self.app.current_user = next((user for user in self.app.users if user["id"] == user_id), None)

        if self.app.current_user:
            from UserDetailsPage import UserDetailsPage
            UserDetailsPage(self.root, self.app)
        else:
            messagebox.showerror("ID Tidak Ditemukan", "ID pengguna tidak ditemukan.")
