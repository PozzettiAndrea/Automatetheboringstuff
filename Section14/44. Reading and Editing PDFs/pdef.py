import os
import PyPDF2

pdf = open("meetingminutes.pdf", "rb")
reader = pyPDF2.PdfFileReader(pdf)
os.system("pause")

print("Number of pages is:", reader.numPages, "\n")

page = reader.getPage(0)
print("The text from the first page is:", page.extractText(), "\n")

os.system("pause")
