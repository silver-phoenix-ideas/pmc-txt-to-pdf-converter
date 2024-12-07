import glob
import pathlib
from fpdf import FPDF

filepaths = glob.glob("files/txt/*.txt")
pdf = FPDF("portrait", "mm", "A4")

for filepath in filepaths:
    # Data
    filename = pathlib.Path(filepath).stem

    with open(filepath) as file:
        content = file.read()

    # Page
    pdf.add_page()

    # Title
    pdf.set_font("Times", "B", 24)
    pdf.cell(0, 10, filename.title(), 0, 1)
    pdf.ln(8)

    # Content
    pdf.set_font("Times", "", 16)
    pdf.multi_cell(0, 8, content)

pdf.output("files/pdf/animals.pdf")
