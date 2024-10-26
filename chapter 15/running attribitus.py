import docx
doc = docx.Document()
doc.add_paragraph('Hello, world!')
docx.text.Paragraph object at 
doc.save('helloworld.docx')
