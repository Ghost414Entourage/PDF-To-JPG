import fitz  # PyMuPDF
import os

def pdf_to_jpeg(pdf_path, output_folder):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)

    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    for page_num in range(len(pdf_document)):
        # Get the page
        page = pdf_document.load_page(page_num)
        
        # Render page to a pixmap
        pix = page.get_pixmap()
        
        # Save the pixmap as a JPEG file
        output_path = os.path.join(output_folder, f'page_{page_num + 1}.jpg')
        pix.save(output_path)

    pdf_document.close()

if __name__ == "__main__":
    pdf_path = '/Users/UserName/Downloads/Volunteer Health History.pdf'  # Path to your PDF file
    output_folder = '/Users/UserName/Downloads/VolunteerHealthImages'     # Folder to save the JPEG files
    pdf_to_jpeg(pdf_path, output_folder)
    print(f"Converted {pdf_path} to JPEG images in {output_folder}")
