# import PyPDF2
# import io

# def extract_text_from_pdf(file_bytes):
#     pdf = PyPDF2.PdfReader(io.BytesIO(file_bytes))
#     text = ""

#     for page in pdf.pages:
#         text += page.extract_text()

#     return text
import PyPDF2
import io

def extract_text_from_pdf(file_bytes):
    pdf = PyPDF2.PdfReader(io.BytesIO(file_bytes))
    text = ""

    for page in pdf.pages:
        page_text = page.extract_text()
        if page_text:   # 🔥 IMPORTANT FIX
            text += page_text + "\n"

    print("EXTRACTED TEXT:", text[:300])  # 🔥 DEBUG

    return text.strip()