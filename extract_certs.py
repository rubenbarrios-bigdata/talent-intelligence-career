import fitz
import sys
import io
import os

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

certs_dir = r"C:\Users\ismar\Downloads\CV_html"

for fname in os.listdir(certs_dir):
    if fname.endswith('.pdf') and fname not in ['Profile.pdf', 'CV_Ruben_Barrios_Data_Analyst.pdf']:
        fpath = os.path.join(certs_dir, fname)
        print(f"\n{'='*60}")
        print(f"CERTIFICADO: {fname}")
        print('='*60)
        try:
            doc = fitz.open(fpath)
            for page in doc:
                print(page.get_text())
            doc.close()
        except Exception as e:
            print(f"Error: {e}")
