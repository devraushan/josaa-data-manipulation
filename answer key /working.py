from PyPDF2 import PdfReader

reader = PdfReader("answer key /rowanswer.pdf")
print(len(reader.pages))
fields = reader.get_form_text_fields()
print(fields)