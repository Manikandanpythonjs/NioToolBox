from tkinter import PhotoImage
import customtkinter
from PIL import Image
from CTkMessagebox import CTkMessagebox
from tkinter import filedialog, StringVar
import aspose.words as aw

# doc = aw.Document("Input.pdf")
# doc.save("Output.txt")


class Compresstopdf(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.selectedpath = StringVar()

        def center_window(self, width, height):
            screen_width = self.winfo_screenwidth()
            screen_height = self.winfo_screenheight()
            x_coordinate = (screen_width - width) // 2
            y_coordinate = (screen_height - height) // 2
            self.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")

        self.title("pdfcompress")
        self._set_appearance_mode("light")
        center_window(self, 300, 200)
        self.resizable(False, False)
        self.configure(fg_color="white")
        self.attributes('-topmost', True)

        self.logotitle = customtkinter.CTkLabel(
            self, text="Choose a pdf file", text_color="grey")
        self.logotitle.pack(padx=10, pady=10, anchor="n")

        self.openfile = customtkinter.CTkButton(
            self, text="Compress a pdf file", command=self.open_file)
        self.openfile.pack(padx=20, pady=20)

        self.selectedpathLabel = customtkinter.CTkLabel(
            self,  text=" ", text_color="grey")
        self.selectedpathLabel.pack(padx=10, pady=10, anchor="n")

    def open_file(self):
        self.attributes('-topmost', False)
        self.file_path = filedialog.askopenfilename(
            filetypes=[("PDF Files", "*.pdf")])
        if self.file_path:

            self.selectedpathLabel.configure(text=self.file_path)
            self.openfile.configure(
                text="Compress PDF", command=self.convertcompresspdf)
            self.selectedpath.set(self.file_path)
            print("Selected file:", self.file_path)
        self.attributes('-topmost', True)

    def convertcompresspdf(self):
        self.wm_attributes("-topmost", False)
        if (self.file_path):

            self.selectedpathLabel.configure(text=self.file_path)

            self.openfile.configure(
                text="Please Wait ....")

            self.output_word_file = filedialog.asksaveasfilename(
                defaultextension=".docx", filetypes=[("PDF Files", "*.pdf")])

            def set_page_size(page_setup, width, height):

                page_setup.page_width = width
                page_setup.page_height = height

            renderer = aw.pdf2word.fixedformats.PdfFixedRenderer()
            pdf_read_options = aw.pdf2word.fixedformats.PdfFixedOptions()
            pdf_read_options.image_format = aw.pdf2word.fixedformats.FixedImageFormat.JPEG
            pdf_read_options.jpeg_quality = 80

            with open(self.file_path, 'rb') as pdf_stream:
                pages_stream = renderer.save_pdf_as_images(
                    pdf_stream, pdf_read_options)

            builder = aw.DocumentBuilder()
            for i in range(0, len(pages_stream)):
                max_page_dimension = 1584
                page_setup = builder.page_setup
                set_page_size(page_setup, max_page_dimension,
                              max_page_dimension)

                page_image = builder.insert_image(pages_stream[i])

                set_page_size(page_setup, page_image.width, page_image.height)
                page_setup.top_margin = 0
                page_setup.left_margin = 0
                page_setup.bottom_margin = 0
                page_setup.right_margin = 0

                if i != len(pages_stream) - 1:
                    builder.insert_break(aw.BreakType.SECTION_BREAK_NEW_PAGE)

            save_options = aw.saving.PdfSaveOptions()
            save_options.cache_background_graphics = True

            builder.document.save(self.output_word_file, save_options)

            self.wm_attributes("-topmost", True)
            self.openfile.configure(
                text="Choose a pdf file", command=self.open_file)

            self.selectedpath.set("")

        else:

            pass
