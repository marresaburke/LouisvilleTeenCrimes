#("/Users/marresaburke/Desktop/Teen-Crimes/LouisvilleTeenCrimes/fiveyrdata.pdf")

import pdfminer.six

from pdfminer.six import extract_text
text = extract_text("fiveyrdata.pdf")

print(text)

#with open("/Users/marresaburke/Desktop/Teen-Crimes/LouisvilleTeenCrimes/fiveyrdata.pdf", 'rb') as pdf_file:
