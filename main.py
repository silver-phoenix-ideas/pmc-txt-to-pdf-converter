import glob
import pathlib
from fpdf import FPDF

filepaths = glob.glob("files/txt/*.txt")
pdf = FPDF("portrait", "mm", "A4")

for filepath in filepaths:
    filename = pathlib.Path(filepath).stem
    pdf.add_page()
    pdf.set_font("Times", "B", 24)
    pdf.cell(0, 10, filename.title(), 0, 1)

pdf.output("files/pdf/animals.pdf")
