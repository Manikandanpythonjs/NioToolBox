from tkinter import PhotoImage
import customtkinter
from PIL import Image
from CTkMessagebox import CTkMessagebox
from tkinter import filedialog, StringVar

from fpdf import FPDF


# doc = aw.Document("Input.pdf")
# doc.save("Output.txt")


class TextToPdf(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.selectedpath = StringVar()

        def center_window(self, width, height):
            screen_width = self.winfo_screenwidth()
            screen_height = self.winfo_screenheight()
            x_coordinate = (screen_width - width) // 2
            y_coordinate = (screen_height - height) // 2
            self.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")

        self.title("texttopdf")
        self._set_appearance_mode("light")
        center_window(self, 300, 200)
        self.resizable(False, False)
        self.configure(fg_color="white")
        self.attributes('-topmost', True)

        self.logotitle = customtkinter.CTkLabel(
            self, text="TEXT TO PDF", text_color="grey")
        self.logotitle.pack(padx=10, pady=10, anchor="n")

        self.openfile = customtkinter.CTkButton(
            self, text="Change Text to Pdf ", command=self.open_file)
        self.openfile.pack(padx=20, pady=20)

        self.selectedpathLabel = customtkinter.CTkLabel(
            self,  text=" ", text_color="grey")
        self.selectedpathLabel.pack(padx=10, pady=10, anchor="n")

    def open_file(self):
        self.attributes('-topmost', False)
        self.file_path = filedialog.askopenfilename(
            filetypes=[("Text Files", "*.txt")])
        if self.file_path:

            self.selectedpathLabel.configure(text=self.file_path)
            self.openfile.configure(
                text="Convert to PDF", command=self.convertpdftoText)
            self.selectedpath.set(self.file_path)
            print("Selected file:", self.file_path)
        self.attributes('-topmost', True)

    def convertpdftoText(self):
        self.wm_attributes("-topmost", False)
        if (self.file_path):

            self.selectedpathLabel.configure(text=self.file_path)

            self.openfile.configure(
                text="Please Wait ....")

            self.output_word_file = filedialog.asksaveasfilename(
                defaultextension=".docx", filetypes=[("PDF Files", "*.pdf")])

      
                    
            
            try:
            
            
                with open(self.file_path, 'r') as file:
                    text = file.read()

                pdf = FPDF()

                pdf.add_page()

                pdf.set_font('Arial', size=12)

                pdf.write(5, text)

                pdf.output(self.output_word_file)

            except Exception as e:
                  CTkMessagebox(
                title="Error", message=str(e), icon="cancel")
          
            self.wm_attributes("-topmost", True)
            self.openfile.configure(
                text="Change Text to Pdf", command=self.open_file)

            self.selectedpath.set("")

        else:

            pass


