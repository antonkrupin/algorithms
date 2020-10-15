from docx import Document

def stringsExchange(fileName, string1, string2):
    
    try:
        document = Document(fileName)
    except Exception:
        return -1

    paragraphs = document.paragraphs

    for x in range(len(paragraphs)):        
        if paragraphs[x].text == string1:
            paragraphs[x].text = string2
            document.save(fileName)
            return 1
    else:
        return -1
        
