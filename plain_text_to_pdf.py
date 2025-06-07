# Converts any plain text file into a simple PDF.

from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

with open("file.txt", "r") as f:
    for line in f:
        pdf.cell(200, 10, txt=line.strip(), ln=1)

pdf.output("file.pdf")
