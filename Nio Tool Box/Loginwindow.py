import customtkinter
import uuid

from PIL import ImageTk, Image
from Signupwindow import SignupWindow
from MainWindow import MainWindow
from DataBaseConnection import get_database
from CTkMessagebox import CTkMessagebox
import socket
from tkinter import messagebox


class LoginWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.uuid = uuid.uuid4()

        self.title("Login")
        self._set_appearance_mode("light")
        self.geometry("1200x600")

        self.configure(fg_color="white")

        self.left_frame = customtkinter.CTkFrame(self, width=300, height=300)
        self.left_frame.pack(side="left")

        image_path = "./src/assets/image/image.png"
        self.image = ImageTk.PhotoImage(Image.open(image_path))
        self.image_label = customtkinter.CTkLabel(
            self.left_frame, image=self.image, text="")  # type: ignore
        self.image_label.pack()

        self.right_frame = customtkinter.CTkFrame(
            self, width=300, height=300)
        self.right_frame.pack(side="left")
        self.right_frame.configure(fg_color="white")

        self.name_for_app = customtkinter.CTkLabel(
            self.right_frame, text="Login to your account",  width=120,
            height=25,
            font=("", 50),
            text_color="#118DF0")
        self.name_for_app.pack(pady=20)

        self.username_entry = customtkinter.CTkEntry(

            self.right_frame, placeholder_text="UserName", border_color="#F9F5F6", text_color="black", corner_radius=10, height=50, width=300, bg_color="white", fg_color="white")
        self.username_entry.pack(padx=30, pady=15)

        self.password_entry = customtkinter.CTkEntry(
            self.right_frame, show="*", placeholder_text="Password", text_color="black", fg_color="white", border_color="#F9F5F6", corner_radius=10, width=300, height=50)
        self.password_entry.pack(padx=30, pady=15)

        self.login_button = customtkinter.CTkButton(
            self.right_frame, text="Login", width=300, cursor="hand2", command=self.login, height=50, corner_radius=10, text_color="white", font=("", 15, "bold"))
        self.login_button.pack(padx=30, pady=15)

        self.signup_name = customtkinter.CTkLabel(
            self.right_frame,  text_color="#118DF0", cursor="hand2", text="Don't have an account Signup", font=("", 16, "bold"))
        self.signup_name.bind("<Button-1>", lambda e: self.signup())
        self.signup_name.pack(pady=10)

    def is_network_connected(self):
        try:
            socket.create_connection(("8.8.8.8", 53), timeout=2)
            return True
        except OSError:
            return False

    def check_network_status(self):
        if self.is_network_connected():
            messagebox.showinfo("Network Status", "Network is connected.")
        else:
            messagebox.showwarning(
                "Network Status", "Network is not connected.")

    def update_network_status(self):
        self.check_network_status()
        self.after(5000, self.update_network_status)

    def signup(self):

        signwin = SignupWindow()

        signwin.mainloop()
        self.destroy()

    def login(self):
        if (self.username_entry.get() == "" and self.password_entry.get() == ""):
            CTkMessagebox(
                title="Error", message="Fields Are Empty . Please Fill the Fields", icon="cancel")

        else:
            dbname = get_database()
            collection_name = dbname["Profile"]

            user_document = collection_name.find_one(
                {"username": self.username_entry.get(), "password": self.password_entry.get()})

            if user_document:
                # User found, do something with the user document
                self.destroy()
                print("User found:", user_document)

                mainwindow = MainWindow()
                mainwindow.mainloop()

            else:

                CTkMessagebox(
                    title="Error", message="User not found or invalid credentials.", icon="cancel")


window = LoginWindow()
window.mainloop()
