import PyPDF2

# Open the PDF file
pdfFileObj = open('C:/Users/pc/Downloads/PDF file.pdf', 'rb')

# Use PdfReader instead of PdfFileReader
pdfReader = PyPDF2.PdfReader(pdfFileObj)

# Access the number of pages, for example
num_pages = len(pdfReader.pages)

num_pagestext = num_pages.extractText(0)
print(num_pagestext)

# Close the file
pdfFileObj.close()

print(f"The PDF has {num_pages} pages.")
