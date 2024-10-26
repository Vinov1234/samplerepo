import PyPDF2
PdfReader = PyPDF2.PdfReader(open("C:/Users/pc/Downloads/PDF file_protected.pdf",'rb'))
print(PdfReader.is_encrypted)
pdfReader.getPage(0)
PdfReader.decrypt('rosebud')
PdfReader.getPage(0)
