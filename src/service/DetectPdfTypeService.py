import os
import pymupdf
import fitz


def is_pdf_scanned(pdf_path):
    doc = fitz.open(pdf_path)
    for page in doc:
        if page.get_text().strip():  # Text exists
            return False
    return True  # No text found on any page = scanned

def classify_pdfs(input_folder):
    scanned = []
    digital = []

    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.pdf'):
            full_path = os.path.join(input_folder, filename)
            if is_pdf_scanned(full_path):
                scanned.append(filename)
            else:
                digital.append(filename)

    return scanned, digital

if __name__ == "__main__":
    folder = "src/data/processed/government"  # Change as needed
    scanned, digital = classify_pdfs(folder)

    print("📄 Scanned PDFs:")
    for s in scanned:
        print(f" - {s}")

    print("\n💻 Digital PDFs:")
    for d in digital:
        print(f" - {d}")
