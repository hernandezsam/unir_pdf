from pathlib import Path
from PyPDF2 import PdfFileMerger, PdfFileReader 


pdf_dir = Path(__file__).parent / "archivos_pdf"


pdf_output_dir = Path(__file__).parent / "PDF Unidos"
pdf_output_dir.mkdir(parents=True, exist_ok=True)


pdf_files = list(pdf_dir.glob("*.pdf"))


keys = set([file.name[:8] for file in pdf_files])


BASE_FILE_NAME_LENGTH = 10

for key in keys:
    merger = PdfFileMerger(strict=False)
    for file in pdf_files:
        if file.name.startswith(key):
            merger.append(PdfFileReader(str(file), "rb" ))
            if len(file.name) >= BASE_FILE_NAME_LENGTH:
                base_file_name = file.name
    merger.write(str(pdf_output_dir / f"{key}.pdf"))
    merger.close()
