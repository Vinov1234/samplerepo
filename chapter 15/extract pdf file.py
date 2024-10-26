import PyPDF2
f = open('C:/Users/pc/Downloads/PDF file.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(f)
# Get the first page
page_one = pdfReader.pages[0]  # Indexing starts from 0 for the first page

# Extract text from the first page
page_one_text = page_one.extract_text()  # Use extract_text() in PyPDF2 v3.0.0

print(page_one_text)
