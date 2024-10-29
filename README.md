Mkdir PDFToJPEGConverter

cd PDFToJPEGConverter

python3 -m venv venv

source venv/bin/activate

pip3 install pdf2image Pillow

pip3 install PyMuPDF

mkdir src

touch src/__init__.py

touch src/pdf_to_jpeg.py

pip3 install PyMuPDF

nano src/pdf_to_jpeg.py

python3 pdf_to_jpeg.py
