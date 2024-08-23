from fpdf import FPDF
from PIL import Image

class Shirtificate:
    def __init__(self, user_name):
        self.user_name = user_name
        self.pdf = FPDF()

    def create_shirtificate(self):
        self.pdf.add_page()
        self.add_title()
        image_y, image_h = self.add_image()
        self.add_text(image_y, image_h)
        self.pdf.output("shirtificate.pdf")

    def add_title(self):
        self.pdf.set_font("Times", 'B', size=30)
        title_text = "CS50 Shirtificate"
        title_width = self.pdf.get_string_width(title_text)
        x_position = (self.pdf.w - title_width) / 2
        self.pdf.set_x(x_position)
        self.pdf.cell(w=title_width, h=10, text=title_text, border=0, align='C')
        self.pdf.ln(20)

    def add_image(self):
        image_path = "shirtificate.png"
        with Image.open(image_path) as img:
            img_width, img_height = img.size
        img_width_mm = img_width * 0.26
        img_height_mm = img_height * 0.26
        x_position_img = (self.pdf.w - img_width_mm) / 2
        current_y = self.pdf.get_y() + 20
        self.pdf.image(image_path, x=x_position_img, y=current_y, w=img_width_mm)
        return current_y, img_height_mm

    def add_text(self, y, h):
        self.pdf.set_font("helvetica", 'B', 25)
        self.pdf.set_text_color(255, 255, 255)
        text = f"{self.user_name} took CS50"
        text_width = self.pdf.get_string_width(text)
        x_position = (self.pdf.w - text_width) / 2
        self.pdf.set_y(y + h / 2 - 20)
        self.pdf.set_x(x_position)
        self.pdf.cell(w=text_width, h=10, text=text, border=0, align='C')

if __name__ == "__main__":
    user_name = input("Enter your username: ")
    shirtificate = Shirtificate(user_name)
    shirtificate.create_shirtificate()
