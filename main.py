from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Create a PDF file with a full black page
pdf_filename = "black_page.pdf"
c = canvas.Canvas(pdf_filename, pagesize=letter)

# Set fill color to black and draw a rectangle covering the whole page
c.setFillColorRGB(0, 0, 0)  # RGB values for black: (0, 0, 0)
c.rect(0, 0, letter[0], letter[1], fill=1)

c.save()

print(f"PDF '{pdf_filename}' created with a full black page.")