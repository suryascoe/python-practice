from pdf2docx import Converter
from pdf2docx import parse

pdf_filepath = 'C:\\Users\\suryasingh04\\OneDrive - Nagarro\\Documents\\How to access your virtual resources.pdf'

docx_filepath = 'C:\\Users\\suryasingh04\\Downloads\\ConvertedDoc.docx'

# To Convert
# try:
#     # Converting PDF to Docx
#     cv_obj = Converter(pdf_filepath)
#     cv_obj.convert(docx_filepath)
#     cv_obj.close()
#
# except():
#     print('Conversion Failed')
#
# else:
#     print('File Converted Successfully')

# To Parse
try:
    # Converting PDF to Docx
    parse(pdf_filepath, docx_filepath)

except():
    print('Conversion Failed')

else:
    print('File Converted Successfully')
