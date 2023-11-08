import customtkinter
from PIL import Image
from CTkMessagebox import CTkMessagebox
from DataBaseConnection import get_database
import uuid
# from Loginwindow import LoginWindow


class SignupWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Signup")
        self._set_appearance_mode("light")
        self.geometry("360x600")
        self.resizable(False, False)
        self.configure(fg_color="white")
        self.uuidID = uuid.uuid4()
        # self.left_frame = customtkinter.CTkFrame(self, width=300, height=300)
        # self.left_frame.pack(side="center")

        # image_path = "./src/assets/image/image.png"
        # self.image = customtkinter.CTkImage(light_image=Image.open(image_path),
        #                                     dark_image=Image.open(image_path), size=(30, 30))
        # self.image_label = customtkinter.CTkLabel(
        #     self.left_frame, image=self.image, text="")  # type: ignore
        # self.image_label.pack()
        self.right_frame = customtkinter.CTkFrame(
            self, width=300, height=300)
        self.right_frame.pack(side="left")
        self.right_frame.configure(fg_color="white", bg_color="white")

        self.name_for_app = customtkinter.CTkLabel(
            self.right_frame, text="Create Your Account",  width=120,
            height=25,
            font=("", 30),
            text_color="#118DF0")
        self.name_for_app.pack(pady=20)

        self.username_entry = customtkinter.CTkEntry(

            self.right_frame, placeholder_text="UserName", border_color="#F9F5F6", text_color="black", corner_radius=10, height=50, width=300, bg_color="white", fg_color="white")
        self.username_entry.pack(padx=30, pady=15)

        self.password_entry = customtkinter.CTkEntry(
            self.right_frame, show="*", placeholder_text="Password", text_color="black", fg_color="white", border_color="#F9F5F6", corner_radius=10, width=300, height=50)
        self.password_entry.pack(padx=30, pady=15)

        self.password_entry_confirm = customtkinter.CTkEntry(
            self.right_frame, show="*", placeholder_text="Confirm Password", text_color="black", fg_color="white", border_color="#F9F5F6", corner_radius=10, width=300, height=50)
        self.password_entry_confirm.pack(padx=30, pady=15)

        self.login_button = customtkinter.CTkButton(
            self.right_frame, text="Create a account", command=self.Signup, width=300, cursor="hand2", height=50, corner_radius=10, text_color="white", font=("", 15, "bold"))
        self.login_button.pack(padx=30, pady=15)

        self.signup_name = customtkinter.CTkLabel(
            self.right_frame, text_color="#118DF0", cursor="hand2", text="Already  Have An Account Login", font=("", 16, "bold"))
        # self.signup_name.bind("<Button-1>", lambda e: self.login)
        self.signup_name.pack(pady=10)

    # def login(self):

    #     lo = LoginWindow()
    #     lo.mainloop()

    def Signup(self):

        if (self.username_entry.get() == "" and self.password_entry.get() == "" and self.password_entry_confirm.get() == ""):
            CTkMessagebox(
                title="Error", message="Fields Are Empty . Please Fill the Fields", icon="cancel")

        elif (self.password_entry.get() != self.password_entry_confirm.get()):

            CTkMessagebox(
                title="Error", message="Password Not Match", icon="cancel")

        else:
            dbname = get_database()
            collection_name = dbname["Profile"]

            mydict = {"username": self.username_entry.get(
            ), "password": self.password_entry.get(), "RefID": str(self.uuidID)}

            x = collection_name.insert_one(mydict)
            self.destroy()
