# EMAIL EXTRACTING
from pypdf import PdfReader
import re

def extract_email(text):

    match = re.search(
        "[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        text
    )

    if match:
        return match.group()

    return None


#PDF READING
def pdf_reader(file_path):
    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:
        text += page.extract_text()

    return text

    