import barcode
from barcode.writer import ImageWriter
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

#CRETAED AND MANTAINED BY GHOST - IGNACIO RIQUELME LAST UPDATE: 26-FEB-2024. 
class CodeBar:
    def __init__(self, data):
        self.data = data
        self.filename = data

    def gen_barcode(self):
        # Create the output directory if it doesn't exist
        output_dir = BASE_DIR / f"static/out/barcode/"
        output_dir.mkdir(parents=True, exist_ok=True)

        # Create a Code128 barcode object
        code128 = barcode.get('code128', self.data, writer=ImageWriter())

        # Save the barcode image to a file
        path_file = output_dir / self.filename
        code128.save(path_file)
        #print(f"Barcode saved as {path_file}")

    def set_data(self, data):
        self.data = data

    def set_filename(self, filename):
        self.filename = filename