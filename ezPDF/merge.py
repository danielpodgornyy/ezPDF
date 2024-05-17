from pypdf import PdfWriter
from pathlib import Path

def MergeFiles(args):

    merger = PdfWriter()
    outputFile = args.output_file

    try:
        for pdf in args.input_files:
            pdf = pdf
            pdfPath = Path(pdf)
            if pdfPath.is_file():
                merger.append(pdf)
            else:
                raise FileNotFoundError
    except FileNotFoundError:
        print(f"error: {pdf} does not exist")
        merger.close()

    merger.write(outputFile)
    merger.close()


