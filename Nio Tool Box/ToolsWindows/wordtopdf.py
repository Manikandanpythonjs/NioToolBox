from tkinter import PhotoImage
import customtkinter
from PIL import Image
from CTkMessagebox import CTkMessagebox
from tkinter import filedialog, StringVar
# from docx2pdf import convert
from docx2pdf import convert

class WORDtoPDF(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.selectedpath = StringVar()

        def center_window(self, width, height):
            screen_width = self.winfo_screenwidth()
            screen_height = self.winfo_screenheight()
            x_coordinate = (screen_width - width) // 2
            y_coordinate = (screen_height - height) // 2
            self.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")

        self.title("wordtopdf")
        self._set_appearance_mode("light")
        center_window(self, 300, 200)
        self.resizable(False, False)
        self.configure(fg_color="white")
        self.attributes('-topmost', True)

        self.logotitle = customtkinter.CTkLabel(
            self, text="WORD TO PDF", text_color="grey")
        self.logotitle.pack(padx=10, pady=10, anchor="n")

        self.openfile = customtkinter.CTkButton(
            self, text="Change word to pdf ", command=self.open_file)
        self.openfile.pack(padx=20, pady=20)

        self.selectedpathLabel = customtkinter.CTkLabel(

            self, text=" ", text_color="grey")
        self.selectedpathLabel.pack(padx=10, pady=10, anchor="n")

    def open_file(self):
        self.attributes('-topmost', False)
        self.file_path = filedialog.askopenfilename(
            filetypes=[("Word Files", "*.docx")]
        )
        if self.file_path:
            self.selectedpathLabel.configure(text=self.file_path)
            self.openfile.configure(
                text="Convert to pdf", command=self.convertwordtopdf)
            self.selectedpath.set(self.file_path)
            print("Selected file:", self.file_path)
            self.attributes('-topmost', True)

    def convertwordtopdf(self):

        if (self.file_path):

            self.openfile.configure(
                text="Please Wait ....")
   
            self.output_pdf_file = filedialog.asksaveasfilename(
                defaultextension=".docx",  filetypes=[("PDF Files", "*.pdf")])
            
            try:
                convert(self.file_path, self.output_pdf_file)
                
            except Exception as e:
                  CTkMessagebox(
                title="Error", message=str(e), icon="cancel")
                

            
            self.openfile.configure(
                text="Change word to pdf", command=self.open_file)

            self.selectedpath.set("")
        else:

            pass


# window = WORDtoPDF()
# window.mainloop()
