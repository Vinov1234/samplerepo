import PyPDF2
f1 = open("C:/Users/pc/Downloads/PDF file_protected.pdf",'rb')
f2 = open('C:/Users/pc/Downloads/PDF file.pdf', 'rb')
Pdf1Reader = PyPDF2.PdfFileReader(pdf1file)
Pdf2Reader = PyPDF2.pdfFileReader(Pdf2File)
PdfWritter = PyPDF2.PdfFileWriter()
for PageNum in range(pdf1Reader.numPages):
    pageObj  = pdf1Reader.getPage(pageNum)
    pdfWriter.addPage(PageOj)
for pageNum in range(pdf2Reader.numPages):
    pageObj = pdf2Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)
pdfOutputFile = open('combineminutes.pdf', 'wb')
pdfWriter.write(pdfOutFile)
pdfOutPutFile.clos()
pdf1File.close()
Pdf2File.close()
