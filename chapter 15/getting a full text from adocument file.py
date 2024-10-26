import docx

def getText(files1):
    doc = docx.Document(files1)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)
