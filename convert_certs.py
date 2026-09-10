import fitz
import os
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

certs_dir = r"C:\Users\ismar\Downloads\CV_html"
output_dir = os.path.join(certs_dir, "certs_images")

os.makedirs(output_dir, exist_ok=True)

cert_files = [
    "Certificado Analisis de Datos IPS DATAX (1).pdf",
    "Certificado IA Leaders (2).pdf",
    "Certificado Power BI-WaveBI.pdf",
    "Certificado Power BI+IA Daxus Latam (1).pdf",
    "Certificado_Iniciacion_Programacion_Python (1).pdf",
    "IBM-Artificial Intelligence Fundamentals (1).pdf",
    "Inteligencia Artificial Aplicada al Trabajo.pdf"
]

for fname in cert_files:
    fpath = os.path.join(certs_dir, fname)
    if os.path.exists(fpath):
        print(f"Convirtiendo: {fname}")
        doc = fitz.open(fpath)
        page = doc[0]
        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
        out_name = fname.replace('.pdf', '.png')
        pix.save(os.path.join(output_dir, out_name))
        doc.close()
        print(f"  -> {out_name}")

print("Listo!")
