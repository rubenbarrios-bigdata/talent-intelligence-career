import fitz
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

files = [
    r"C:\Users\ismar\Downloads\CV_html\Profile.pdf",
    r"C:\Users\ismar\Downloads\CV_html\CV_Ruben_Barrios_Data_Analyst.pdf"
]

for f in files:
    print(f"\n{'='*60}")
    fname = f.split('\\')[-1]
    print(f"ARCHIVO: {fname}")
    print('='*60)
    doc = fitz.open(f)
    for page in doc:
        print(page.get_text())
    doc.close()
