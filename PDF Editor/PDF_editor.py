import PyPDF2
import sys

inputs = sys.argv[1:]


#PDF mereger
def pdfmerger(pdf_list):
	merger = PyPDF2.PdfFileMerger()
	for pdf in pdf_list:
		print(pdf)
		merger.append(pdf)
	merger.write('main1.pdf')

pdfmerger(inputs)


#Rotation of pdf
import PyPDF2

with open('main2.pdf', 'rb') as file: # we have to use 'rb' i.e. read binary -  it is a standard and have to be remembered
	reader = PyPDF2.PdfFileReader(file) #need to read the documentation for knowing about the methods used
	
	page = reader.getPage(0)
	page.rotateClockwise(-90)
	writer = PyPDF2.PdfFileWriter()
	writer.addPage(page)
	with open('tilt.pdf', 'wb') as new_file:
		writer.write(new_file)

#Adding watermark to pdfs

import PyPDF2

template = PyPDF2.PdfFileReader(open('main3.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()


for i in range(template.getNumPages()):
	page = template.getPage(i)
	page.mergePage(watermark.getPage(0))
	output.addPage(page)


	with open('WMpdf.pdf', 'wb') as file:
		output.write(file)