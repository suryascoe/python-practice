from pdf2docx import Converter
from pdf2docx import parse

pdf_filepath = 'Your PDF File path - Replace "\" with "\\"'

docx_filepath = 'Your Docx File path - Replace "\" with "\\"'

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
