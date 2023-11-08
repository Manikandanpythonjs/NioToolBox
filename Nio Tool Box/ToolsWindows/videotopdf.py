from tkinter import PhotoImage
import customtkinter
from PIL import Image
from CTkMessagebox import CTkMessagebox
from tkinter import filedialog, StringVar
import cv2
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
# doc = aw.Document("Input.pdf")
# doc.save("Output.txt")


class VideoToPDF(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.selectedpath = StringVar()

        def center_window(self, width, height):
            screen_width = self.winfo_screenwidth()
            screen_height = self.winfo_screenheight()
            x_coordinate = (screen_width - width) // 2
            y_coordinate = (screen_height - height) // 2
            self.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")

        self.title("videotopdf")
        self._set_appearance_mode("light")
        center_window(self, 300, 200)
        self.resizable(False, False)
        self.configure(fg_color="white")
        self.attributes('-topmost', True)

        self.logotitle = customtkinter.CTkLabel(
            self, text="VIDEO TO PDF", text_color="grey")
        self.logotitle.pack(padx=10, pady=10, anchor="n")

        self.openfile = customtkinter.CTkButton(
            self, text="Choose video ", command=self.open_file)
        self.openfile.pack(padx=20, pady=20)

        self.selectedpathLabel = customtkinter.CTkLabel(
            self,  text=" ", text_color="grey")
        self.selectedpathLabel.pack(padx=10, pady=10, anchor="n")

    def open_file(self):
        self.attributes('-topmost', False)
        self.file_path = filedialog.askopenfilename(
            filetypes=[("video Files", "*.mp4")])
        if self.file_path:

            self.selectedpathLabel.configure(text=self.file_path)
            self.openfile.configure(
                text="Convert to PDF", command=self.converttexttoword)
            self.selectedpath.set(self.file_path)
            print("Selected file:", self.file_path)
        self.attributes('-topmost', True)

    def converttexttoword(self):
        self.wm_attributes("-topmost", False)
        if (self.file_path):

            self.selectedpathLabel.configure(text=self.file_path)

            self.openfile.configure(
                text="Please Wait ....")

            self.output_word_file = filedialog.asksaveasfilename(
                defaultextension=".docx", filetypes=[("PDF Files", "*.pdf")])

            cap = cv2.VideoCapture(self.file_path)
            frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

            pdf = canvas.Canvas(self.output_word_file, pagesize=letter)

            for i in range(frame_count):
                # Read a frame from the video
                ret, frame = cap.read()

                # Convert the frame to grayscale (optional)
                # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                # Save the frame as an image (e.g., PNG)
                image_filename = f"frame_{i}.png"
                cv2.imwrite(image_filename, frame)

                # Draw the image on the PDF
                pdf.drawImage(image_filename, 0, 0,
                              width=letter[0], height=letter[1])

                # Add a new page for each frame
                pdf.showPage()

            self.wm_attributes("-topmost", True)
            self.openfile.configure(
                text="Choose a video", command=self.open_file)

            self.selectedpath.set("")

        else:

            pass
