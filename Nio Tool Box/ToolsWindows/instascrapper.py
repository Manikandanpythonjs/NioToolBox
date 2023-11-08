from tkinter import PhotoImage
import customtkinter
from PIL import Image
from CTkMessagebox import CTkMessagebox
from tkinter import filedialog, StringVar

import instaloader


# doc = aw.Document("Input.pdf")
# doc.save("Output.txt")


class InstaScrapper(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.selectedpath = StringVar()

        def center_window(self, width, height):
            screen_width = self.winfo_screenwidth()
            screen_height = self.winfo_screenheight()
            x_coordinate = (screen_width - width) // 2
            y_coordinate = (screen_height - height) // 2
            self.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")

        self.title("InstaScrapper")
        self._set_appearance_mode("light")
        center_window(self, 300, 200)
        self.resizable(False, False)
        self.configure(fg_color="white")
        self.attributes('-topmost', True)

        self.logotitle = customtkinter.CTkLabel(
            self, text="Download Insta Source", text_color="grey")
        self.logotitle.pack(padx=10, pady=10, anchor="n")

        self.username_entry = customtkinter.CTkEntry(

            self, placeholder_text="UserName", border_color="#F9F5F6", text_color="black", corner_radius=10, height=50, width=300, bg_color="white", fg_color="white")
        self.username_entry.pack(padx=30, pady=15)

        self.openfile = customtkinter.CTkButton(
            self, text="Get Source", command=self.instasource)
        self.openfile.pack(padx=20, pady=20)

        self.selectedpathLabel = customtkinter.CTkLabel(
            self,  text=" ", text_color="grey")
        self.selectedpathLabel.pack(padx=10, pady=10, anchor="n")

    def instasource(self):

        self.source = self.username_entry.get()

        if (self.source == ""):

            CTkMessagebox(
                title="Error", message="Fields Are Empty . Please Fill the Fields", icon="cancel")
        else:

            try:
                instaloader.Instaloader().download_profile(self.source, profile_pic_only=False)

            except Exception as e:

                CTkMessagebox(
                    title="Error", message=str(e), icon="cancel")
