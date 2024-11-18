# Adjust the text for a two-column layout to match the images

# Create the PDF with two columns layout
pdf = FPDF()

# Function to add text in two-column format
def add_two_column_text(pdf, text_left, text_right):
    # Left column
    pdf.set_xy(10, pdf.get_y())  # Set position for left column
    pdf.multi_cell(90, 10, text_left, align='L')
    
    # Right column
    pdf.set_xy(110, pdf.get_y() - 90)  # Set position for right column
    pdf.multi_cell(90, 10, text_right, align='L')

# Add a page
pdf.add_page()
pdf.set_font("Arial", size=10)

# Break the text into left and right columns
lines = normalized_text.split("\n\n")
for i in range(0, len(lines), 2):
    left_column = lines[i].strip()
    right_column = lines[i + 1].strip() if i + 1 < len(lines) else ''
    add_two_column_text(pdf, left_column, right_column)

# Save the PDF
pdf_output_path = "/mnt/data/extracted_text_two_column_layout.pdf"
pdf.output(pdf_output_path)

# Return the path to the generated PDF file
pdf_output_path
