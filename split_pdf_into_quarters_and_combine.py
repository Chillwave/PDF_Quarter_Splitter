from PyPDF2 import PdfWriter, PdfReader
import os
import datetime

def split_pdf_into_quarters_and_combine(pdf_path, output_folder):
    # Ensure the output directory exists
    os.makedirs(output_folder, exist_ok=True)

    reader = PdfReader(pdf_path)
    num_pages = len(reader.pages)

    # Create a single PDF writer to store all the quarters
    writer = PdfWriter()

    for page_number in range(num_pages):
        page = reader.pages[page_number]
        original_width = page.mediabox.width
        original_height = page.mediabox.height
        
        # Define crop boxes for each quarter
        quarters = {
            "NW": (0, original_height / 2, original_width / 2, original_height),
            "NE": (original_width / 2, original_height / 2, original_width, original_height),
            "SW": (0, 0, original_width / 2, original_height / 2),
            "SE": (original_width / 2, 0, original_width, original_height / 2),
        }

        for quarter_name, (x1, y1, x2, y2) in quarters.items():
            # Create a separate page instance for each quarter to avoid altering the same page
            cropped_page = reader.pages[page_number]
            cropped_page.mediabox.lower_left = (x1, y1)
            cropped_page.mediabox.upper_right = (x2, y2)
            
            # Add cropped page to the writer
            writer.add_page(cropped_page)

    # Timestamp for the output filename
    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    output_pdf_path = os.path.join(output_folder, f"combined_quarters_{timestamp}.pdf")
    with open(output_pdf_path, 'wb') as output_pdf_file:
        writer.write(output_pdf_file)

    print(f"All quarters saved into a single file: {output_pdf_path}")

# Usage
pdf_path = "input.pdf"  # or the path to your PDF
output_folder = "output_quarters"
split_pdf_into_quarters_and_combine(pdf_path, output_folder)
