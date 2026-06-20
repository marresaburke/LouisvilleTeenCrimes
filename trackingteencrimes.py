#("/Users/marresaburke/Desktop/Teen-Crimes/LouisvilleTeenCrimes/fiveyrdata.pdf")

from pypdf import PdfReader

# Load your PDF file
reader = PdfReader("fiveyrdata.pdf")

# Extract and print text from all pages
for page_num, page in enumerate(reader.pages):
    text = page.extract_text()
    print(f"--- Page {page_num + 1} ---")
    print(text)

 #This code - shows me there are 150 pages of this document 


#with open("/Users/marresaburke/Desktop/Teen-Crimes/LouisvilleTeenCrimes/fiveyrdata.pdf", 'rb') as pdf_file:


