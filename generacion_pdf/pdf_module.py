from generacion_pdf.barcode_module import CodeBar
from generacion_pdf.xml_module import XMLReader
from datetime import datetime
from fpdf import FPDF
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

#CRETAED AND MANTAINED BY GHOST - IGNACIO RIQUELME LAST UPDATE: 26-FEB-2024. 
class PDF(FPDF):
    # Global document config properties
    MARGIN_LEFT = 10
    MARGIN_RIGHT = 10
    FONT_SIZE_NORMAL = 10
    FONT_SIZE_TITLE = 14
    FONT_SIZE_SUBTITLE = 12
    FONT_SIZE_TABLE =7
    NO_POLIZA = ""

    def header(self):
        logo_path = BASE_DIR / "static/images/bciLogo.png"
        logo_width = 50  # Adjust as needed
        self.image(logo_path, self.w / 2 - logo_width / 2, 10, logo_width)
        self.ln(20)

    def footer(self):
        # Position cursor at 1.5 cm from bottom:
        self.set_y(-15)
        # Setting font: helvetica italic 8
        self.set_font("helvetica", "I", 8)
        # Printing page number:
        self.cell(0, 10, f"{self.page_no()}", align="C")

    def set_no_policy(self, noPoliza):
        self.NO_POLIZA = noPoliza

    def set_left_margin(self, margin):
        self.l_margin = margin

    def set_right_margin(self, margin):
        self.r_margin = margin

    def set_title(self, title):
        self.ln(1)
        self.set_font("helvetica", "B", self.FONT_SIZE_TITLE)
        self.cell(0, 0, title, align="C")
        self.ln(1)

    def set_subtitle(self, subtitle, align):
        self.ln(1)
        self.set_font("helvetica", "B", size=self.FONT_SIZE_SUBTITLE)
        self.cell(0, 0, subtitle, align=align)
        self.ln(1)

    def set_paragraph(self, paragraph):
        self.ln(1)
        left_margin = self.MARGIN_LEFT
        right_margin = self.MARGIN_RIGHT
        self.set_font("helvetica", size=self.FONT_SIZE_NORMAL)
        self.set_left_margin(left_margin)
        self.set_right_margin(right_margin)        
        self.multi_cell(0, 5, paragraph, align="J")
        self.ln(1)

    def set_table_col3(self, data):
        self.ln(1)
        self.set_font("helvetica", style='B', size=self.FONT_SIZE_NORMAL)
        #self.set_font("helvetica", size=self.FONT_SIZE_NORMAL)
        left_margin = self.MARGIN_LEFT
        right_margin = self.MARGIN_RIGHT
        available_width = self.w - left_margin - right_margin
        #print(available_width)
        col_widths = [65, 65, 65]
        cell_width = available_width / len(col_widths)

        for row in data:
            for i, text in enumerate(row):
                border = "TB" if i == 1 else "LTB" if i == 0 else "RTB" if i == 2 else ""
                self.cell(col_widths[i], 5, text, border=border)
            self.ln(5)
        self.ln(1)

    def set_table_col2(self, data, subtitle):
        self.ln(1)
        if subtitle and subtitle != "":
            self.set_subtitle(subtitle,"L")
            self.ln(1)

        self.set_font("helvetica", size=self.FONT_SIZE_NORMAL)
        left_margin = self.MARGIN_LEFT
        right_margin = self.MARGIN_RIGHT
        available_width = self.w - left_margin - right_margin
        col_widths = [97.5, 97.5]
        cell_width = available_width / len(col_widths)

        c = 1
        for row in data:
            for i, text in enumerate(row, start=0):
                border = ""
                if c == 1:
                    if i == 0:
                        border = "LT"
                    elif i == 1:
                        border = "RT"
                elif c != 1 and c != len(data):
                    if i == 0:
                        border = "L"
                    elif i == 1:
                        border = "R"
                if c == 1 and c == len(data):
                    if i == 0:
                        border = "BLT"
                    elif i == 1:
                        border = "BRT"
                elif c == len(data):
                    if i == 0:
                        border = "LB"
                    elif i == 1:
                        border = "RB"

                self.cell(col_widths[i - 1], 5, str(text), border=border)
            self.ln(5)
            c += 1
        self.ln(1)

    def set_coverages(self, data):
        left_margin = self.MARGIN_LEFT
        right_margin = self.MARGIN_RIGHT
        self.set_left_margin(left_margin)
        self.set_right_margin(right_margin)
        self.set_font("helvetica", size=self.FONT_SIZE_TABLE)

        total_width = self.w - (left_margin + right_margin)
        num_columns = len(data[0])

        # Define the percentage of total width for the first column
        first_column_percentage = 0.32

        # Calculate the actual width for the first column
        first_column_width = round(total_width * first_column_percentage)

        # Calculate the minimum width for each column
        min_column_width = 20  # You can adjust this value based on your layout requirements

        # Calculate the width available for the other columns
        other_columns_width = max(round((total_width - first_column_width) / (num_columns - 1)), min_column_width)

        # Add table headers
        self.set_font("helvetica", style='B', size=self.FONT_SIZE_TABLE)

        self.cell(first_column_width, 4, data[0][0], border="B")
        for i in range(1, num_columns):
            self.cell(other_columns_width, 4, data[0][i], border="B")
        self.ln(4)

        # Add table data
        for row in data[1:]:
            self.cell(first_column_width, 4, str(row[0]), border="B")
            for i in range(1, num_columns):
                self.cell(other_columns_width, 4, str(row[i]), border="B")
            self.ln(4)

    def set_col2_content_left(self, data, subtitle, border_none):
        self.ln(1)
        if subtitle and subtitle != "":
            self.ln(1)
            self.set_font("helvetica", "B", size=self.FONT_SIZE_SUBTITLE)
            x=130
            if(subtitle=="CORREDOR"):
               x=125 
            self.cell(x, 0, subtitle,align="R")
            self.ln(1)

        left_margin = self.MARGIN_LEFT
        right_margin = self.MARGIN_RIGHT
        self.set_left_margin(left_margin)
        self.set_right_margin(right_margin)
        available_width = self.w - left_margin - right_margin
        col_widths = [97.5,97.5]
        cell_width = available_width / len(col_widths)
        self.set_font("helvetica", size=self.FONT_SIZE_NORMAL)
        align ="L"
        img=""
        codebar= True
        self.ln(1)
        if(border_none == 0):
            c=1
            for row in data:
                for i, text in enumerate(row, start=0):
                    if(i==0):
                        align = "C"
                        border = ""
                        self.set_font("helvetica", style='B', size=self.FONT_SIZE_SUBTITLE)
                        img = BASE_DIR / "static/images/SignVida.png"
                        self.set_image(self.get_x()+25, self.get_y()-30,0,0, img)
                    elif(i==1):
                        img = BASE_DIR / f"static/out/barcode/{self.NO_POLIZA}.png"
                        
                        if(codebar != False):
                            self.set_image(self.get_x()+20, self.get_y()+5,60,18, img)
                            codebar = False
                    else:
                        align="L"
                        self.set_font("helvetica", style='B', size=self.FONT_SIZE_NORMAL)
                    self.multi_cell(col_widths[i-1], 5, str(text), border=border,align =align)
                self.ln(5)
                c=c+1
            self.ln(1)            
        elif(border_none == 1):
            c=1
            for row in data:
                for i, text in enumerate(row, start=0):
                    border = ""
                    if(c==1):
                        if(i==0):
                            border = ""
                        elif(i==1):
                            border = "LTR"
                    elif(c!=1 & c!=len(data)):
                        if(i==0):
                            border = ""
                        elif(i==1):
                            border = "LR"                      
                                    
                    if(c==2):
                        if(i==0):
                            text=""
                    if(c == len(data)):
                        if(i==0):
                            border = ""
                        elif(i==1):
                            border ="LBR"

                    self.cell(col_widths[i-1], 5, str(text), border=border,align=align)
                self.ln(5)
                c=c+1
            self.ln(1)

    def set_additional_insured(self, data, subtitle):
        # Add a line break
        self.ln(1)

        # Check if subtitle is provided and not empty
        if subtitle and subtitle != "":
            # Set the subtitle using the custom set_subtitle method with alignment "L"
            self.set_subtitle(subtitle, "L")
            # Add another line break
            self.ln(1)

        # Set font to "helvetica" with size 9
        self.set_font("helvetica", size=9)

        # Define left and right margins
        left_margin = self.MARGIN_LEFT
        right_margin = self.MARGIN_RIGHT

        # Calculate the available width for the content
        available_width = self.w - left_margin - right_margin

        # Define column widths for the table
        col_widths = [48.75, 48.75, 48.75, 48.75]

        # Calculate the width of each cell
        cell_width = available_width / len(col_widths)

        # Initialize a counter variable for tracking rows
        c = 1

        # Iterate through each row in the provided data
        for row in data:
            # Iterate through each element in the row
            for i, text in enumerate(row, start=0):
                # Get the appropriate border style using the custom get_border_asegurados method
                border = self.get_border_asegurados(c, i, len(data))
                # Add a cell with the current element's text, specified width, and calculated border
                self.cell(col_widths[i - 1], 5, str(text), border=border, align="C")
            
            # Add a line break after each row
            self.ln(5)
            # Increment the counter for the next row
            c += 1

        # Add an extra line break at the end
        self.ln(1)

    def get_border_asegurados(self, c, i, data_length):
        border = ""
        if c == 1:
            if i == 0:
                border = "LT"
            elif 0 < i < 3:
                border = "T"
            elif i == 3:
                border = "RT"
        elif 1 < c < data_length:
            if i == 0:
                border = "L"
            elif i == 3:
                border = "R"
        if c == 1 and c == data_length:
            if i == 0:
                border = "BLT"
            elif i == 1 or i == 2:
                border = "TB"
            elif i == 3:
                border = "BRT"
        elif c == data_length:
            if i == 0:
                border = "LB"
            elif i == 1 or i == 2:
                border = "B"
            elif i == 3:
                border = "RB"
        return border
    
    def set_image(self,image_x, image_y, image_width, image_height,image_path):
        self.image(image_path, x=image_x, y=image_y, w=image_width, h=image_height)

    def gen_pdf_vida(self,xml_path):
        # Instantiation xml reader
        reader = XMLReader(xml_path)

        # Xml data to dict and array of coverages
        coverages = reader.get_coverages_to_list()
        data_xml = reader.get_xml_to_dict()
        
        # Add new page
        self.add_page()
        noPoliza = data_xml["POLIZA"]
        print(f"Inicio Generacion Pdf: {noPoliza} {str(datetime.now())}")
        
        # Set data
        data_policy = {
            "title": f"{data_xml["TITULO"]}",
            "paragraph": """BCI Seguros Vida S.A., en consideración a la Propuesta de Seguro presentada por el contratante y/o asegurado, su Declaración de Salud si corresponde, las Condiciones Generales respectivas y las Condiciones Particulares que a continuación se detallan, acepta por medio de la presente póliza en asegurar lo siguiente:""",
            "data": [
                    [f"SUCURSAL : {data_xml["SUCURSAL"]}", f"PROPUESTA N°: {data_xml["PROPUESTA"]}", f"PÓLIZA N°: {data_xml["POLNRO"]}"]
                ],
                "contratante": [
                    [f"Nombre : {data_xml["NOMBRE"]}",f"Rut : {data_xml["RUTCON"]}"],
                    [f"Direccion : {data_xml["DIRECCION"]}", f""],
                    [f"Comuna: {data_xml["COMUNA"]}", f"Ciudad: {data_xml["CIUDAD"]}"],
                    [f"Telefono: {data_xml["TELEFONO"]}", f"E-Mail: {data_xml["EMAIL"]}"]
                ],
                "aseguradoTitular": [
                    [f"Nombre : {data_xml["NOMBREASEG"]}", f"Rut : {data_xml["RUTASEG"]}"],
                    [f"Direccion : {data_xml["DIRECCIONASEG"]}", f""],
                    [f"Comuna: {data_xml["COMUNAASEG"]}", f"Ciudad: {data_xml["CIUDADASEG"]}"],
                    [f"Telefono: {data_xml["TELEFONOASEG"]}", f"Fecha de Nacimiento: {data_xml["FECNACASEG"]}"]
                ],
                "vigenciaSeguro": [
                    [f"Desde : {data_xml["VIG_INI"]}", f"Hasta : {data_xml["VIG_FIN"]}"],
                ],
                "plan": [
                    [f"Plan : {data_xml["PLAN_DESCRIPCION"]}", ""],
                ],
                "primasTotales": [
                    [f"Primas Totales : Exenta UF {data_xml["EXENTA"]}", f"Afecta UF : {data_xml["AFECTA"]}"],
                    [f"                                IVA UF : {data_xml["IVA"]}", f" Bruta UF : {data_xml["BRUTA"]}"]
                ],
                "coverages": coverages,
                "dataPagoPrima": [
                    [f"", f"Periodicidad de Pago : {data_xml["PERPAGO"]}"],
                    [f"./bciLogo.png", f"Forma de Pago : {data_xml["FRMPAGO"]}"],
                    [f"", f"Día de Pago : {data_xml["DPAGO"]}"]
                ],
                "dataCorredor": [
                    [f"", f"R.U.T : {data_xml["RUTCOR"]}"],
                    [f"./bciLogo.png", f"Nombre : {data_xml["NBCOR"]}"],
                    [f"", f"Comisión del Corredor : {data_xml["COMCOR"]}"]
                ],
                "dataEmision": [
                    [f"BCI SEGUROS VIDA S.A.", f"Fecha de Emisión : {data_xml["FEMI"]}"]
                ],
                "aseguradosAdicionales": [
                    ["Nombres", "Rut", "Fecha de Nacimiento", "Relación"],
                    ["", "", "", ""],
                    ["", "", "", ""],
                    ["", "", "", ""]
                ]
        }

        # Initialize the CodeBar object
        codebar = CodeBar(noPoliza)
        codebar.gen_barcode()    

        # Adding content to pdf class
        self.set_no_policy(f"{data_xml["POLIZA"]}")
        self.set_title(data_policy["title"])
        self.set_paragraph(data_policy["paragraph"])
        self.set_table_col3(data_policy["data"])
        self.set_table_col2(data_policy["contratante"],"CONTRATANTE")
        self.set_table_col2(data_policy["aseguradoTitular"],"ASEGURADO TITULAR")
        self.set_table_col2(data_policy["vigenciaSeguro"],"VIGENCIA DEL SEGURO")
        self.set_table_col2(data_policy["plan"],"PLAN, coverages Y PRIMA")
        self.set_coverages(data_policy["coverages"])
        self.set_table_col2(data_policy["primasTotales"],"")
        self.set_col2_content_left(data_policy["dataPagoPrima"],"PAGO PRIMAS",1)
        self.set_col2_content_left(data_policy["dataCorredor"],"CORREDOR",1)
        self.set_col2_content_left(data_policy["dataEmision"],"",0)
        
        # Set new page
        self.add_page()

        # Add more content to new page
        self.set_additional_insured(data_policy["aseguradosAdicionales"],"ASEGURADOS ADICIONALES")


        # Write pdf
        pdf_output = BASE_DIR / f"static/out/pdf/vida/{noPoliza}.pdf"
        self.output(pdf_output)
        
        print(f"Fin Generacion Pdf: {noPoliza} {str(datetime.now())}")