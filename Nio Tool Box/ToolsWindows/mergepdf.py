from tkinter import PhotoImage
import customtkinter
from PIL import Image
from CTkMessagebox import CTkMessagebox
from tkinter import filedialog, StringVar
import aspose.words as aw
from PyPDF2 import PdfMerger


# doc = aw.Document("Input.pdf")
# doc.save("Output.txt")


class MergePdf(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.selectedpath = StringVar()

        def center_window(self, width, height):
            screen_width = self.winfo_screenwidth()
            screen_height = self.winfo_screenheight()
            x_coordinate = (screen_width - width) // 2
            y_coordinate = (screen_height - height) // 2
            self.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")

        self.title("mergepdf")
        self._set_appearance_mode("light")
        center_window(self, 300, 200)
        self.resizable(False, False)
        self.configure(fg_color="white")
        self.attributes('-topmost', True)

        self.logotitle = customtkinter.CTkLabel(
            self, text="Choose pdfs", text_color="grey")
        self.logotitle.pack(padx=10, pady=10, anchor="n")

        self.openfile = customtkinter.CTkButton(
            self, text="MERGE PDF", command=self.open_file)
        self.openfile.pack(padx=20, pady=20)

        self.selectedpathLabel = customtkinter.CTkLabel(
            self,  text=" ", text_color="grey")
        self.selectedpathLabel.pack(padx=10, pady=10, anchor="n")

    def open_file(self):
        self.attributes('-topmost', False)
        self.file_path = filedialog.askopenfilenames(
            filetypes=[("PDF Files", "*.pdf")])
        if self.file_path:

            self.selectedpathLabel.configure(text=self.file_path)
            self.openfile.configure(
                text="MERGE PDF", command=self.convertmergepdf)
            self.selectedpath.set(self.file_path)
            print("Selected file:", self.file_path)
        self.attributes('-topmost', True)

    def convertmergepdf(self):
        self.wm_attributes("-topmost", False)
        self.files = []
        if (self.file_path):

            self.selectedpathLabel.configure(text=self.file_path)

            self.openfile.configure(
                text="Please Wait ....")
            self.output_word_file = filedialog.asksaveasfilename(
                defaultextension=".docx", filetypes=[("PDF Files", "*.pdf")])

            merger = PdfMerger()

            self.files = self.file_path

            for pdf_file in self.files:
                with open(pdf_file, 'rb') as file:
                    merger.append(file)

            with open(self.output_word_file, 'wb') as output_file:
                merger.write(output_file)

            self.wm_attributes("-topmost", True)
            self.openfile.configure(
                text="Choose PDFs", command=self.open_file)

            self.selectedpath.set("")

        else:

            pass
