from pdf2docx import Converter
pdf_file = "epm_radicar.pdf"
docx_file = "epm_radicar.docx"
cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()
