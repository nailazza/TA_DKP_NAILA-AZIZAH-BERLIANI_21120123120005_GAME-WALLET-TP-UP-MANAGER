import customtkinter as ctk
from InitialPage import InitialPage

class TopUpApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Top Up Application")
        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("green")
        self.root.geometry("393x400")

        # Sample user data
        self.users = [
            {"id": "A1B2C3D4", "username": "user_A1B2", "diamonds": 10, "history": []},
            {"id": "E5F6G7H8", "username": "user_E5F6", "diamonds": 20, "history": []},
            {"id": "I9J0K1L2", "username": "user_I9J0", "diamonds": 30, "history": []},
            {"id": "M3N4O5P6", "username": "user_M3N4", "diamonds": 40, "history": []},
            {"id": "Q7R8S9T0", "username": "user_Q7R8", "diamonds": 50, "history": []},
        ]
        self.current_user = None

        self.show_initial_page()

    def show_initial_page(self):
        InitialPage(self.root, self)

if __name__ == "__main__":
    root = ctk.CTk()
    app = TopUpApp(root)
    root.mainloop()
