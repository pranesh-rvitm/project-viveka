from libretranslatepy import LibreTranslateAPI
from fpdf import FPDF
from PyPDF2 import PdfReader
import argparse

def argument():
    parser = argparse.ArgumentParser(description='Description of your program')
    # Add a single string argument to the parser
    parser.add_argument('-a', '--argument', type=str, help='language to be translated to') # Access the argument value
    language = str(parser.parse_args().argument)
    # Use the argument value in your code
    print('Language as argument :',language)
    if language=='None':
        language = input('Enter language')
        return language
    return language


def read_pdf(file_path):
    pdfFileObj = open(file_path, 'rb')
    pdfreader = PdfReader(pdfFileObj)
    extracted_text = ''

    for pageObj in pdfreader.pages:
        extracted_text += pageObj.extract_text()

    pdfFileObj.close()
    print(extracted_text)
    return extracted_text


def translate(text, source_lang, language):
    translator = LibreTranslateAPI()
    translated_text = translator.translate(text, source_lang, language)
    print(translated_text)
    return translated_text


def write_pdf(output_path, translated_text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=11)

    paragraphs = translated_text.split('\n')
    for p in paragraphs:
        pdf.multi_cell(0, 5, p)
        pdf.ln()

    pdf.output(output_path)


def translate_pdf(input_file, output_file, source_lang):
    lang=argument()
    extracted_text = read_pdf(input_file)
    translated_text = translate(extracted_text, 'auto', lang)
    write_pdf(output_file, translated_text)



input_file = 'sample1.pdf'
output_file = 'output.pdf'
source_lang = 'auto'
translate_pdf(input_file, output_file, source_lang)
