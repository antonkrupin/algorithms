import os
from PIL import Image, ImageDraw, ImageColor, ImageFont

def changeImgType(fileExtension, fileExtensionToChange):
    isFilesInDirectory = False
    directory = os.getcwd()
    
    fileExtension = fileExtension.lower()
    fileExtensionToChange = fileExtensionToChange.lower()

    if fileExtension[0] != '.':
        fileExtension = '.' + fileExtension
    
    if fileExtensionToChange[0] == '.':
        fileExtensionToChange = fileExtensionToChange[1:]
    
    for i in os.walk(directory):    
        for file in i[2]:
            if os.path.splitext(file)[1] == fileExtension:
                if isFilesInDirectory == False:
                    isFilesInDirectory = True
                    img = Image.open(file)
                    if img.mode == 'RGB':
                        drawRectangleAndText(img).save(file.replace(fileExtension[1:], fileExtensionToChange))
                    else:
                        img_rgb = img.convert('RGB')
                        drawRectangleAndText(img_rgb).save(file.replace(fileExtension[1:], fileExtensionToChange))
                    os.remove(file)
                else:
                    img = Image.open(file)
                    if img.mode == 'RGB':
                        drawRectangleAndText(img).save(file.replace(fileExtension[1:], fileExtensionToChange))
                    else:
                        img_rgb = img.convert('RGB')
                        drawRectangleAndText(img_rgb).save(file.replace(fileExtension[1:], fileExtensionToChange))
                    os.remove(file)
    
    if isFilesInDirectory:
        return 1
    else:
        return -1 

def drawRectangleAndText(img):
    draw = ImageDraw.Draw(img)
    W, H = img.size

    draw.rectangle([W/2 - 150, H/2 - 150, W/2 + 150, H/2 + 150], 
                    fill=None, outline=(125,56,168), width=10)

    font = ImageFont.truetype('arial.ttf', 50)

    message = 'Hellow\nWorld!'
    
    draw.multiline_text([W/2 - 50, H/2 - 50], 
                        message, fill=(255,165,0), font=font)

    return img


