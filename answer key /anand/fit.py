import fitz
doc = fitz.open('rowpdf.pdf')
txt = ""
for page in doc:
    text = page.get_text("block")
    text += "\n"
    txt+=text

file1 = open('textdata.txt','w')
file1.write(txt)
file1.close()
# page = doc[0]
# text = page.get_text("block")
# # file = open("try.json","w")
# # file.write(text)
# file = open("try.txt","w")
# file.write(text)
# print(text) 