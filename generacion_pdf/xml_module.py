import json
import xml.etree.ElementTree as ET

#CRETAED AND MANTAINED BY GHOST - IGNACIO RIQUELME LAST UPDATE: 26-FEB-2024.
class XMLReader:
    FILE_PATH = ""

    def __init__(self, file_path):
        self.FILE_PATH = file_path
        tree = ET.parse(self.FILE_PATH)
        root = tree.getroot()
        #print("self.FILE_PATH : "+self.FILE_PATH)

    def get_coverages_to_list(self):
        coberageList = [] 
        #xml file path
        archivo_xml = self.FILE_PATH
        #read xml file utf-8
        tree = ET.parse(archivo_xml,parser=ET.XMLParser(encoding="utf-8"))
        root = tree.getroot()

        #set header for data return
        coberageList.append(["Coberturas", "Capital", "Asegurado", "Prima", "Bruta Mensual", "Límite de Edad", "Registro C.M.F"])
        
        #set content to data return
        for element in root.findall('CAR/CAR.COBERTURAS/COB.DET'):
            dataRow = []
            for row in element.iter():  
                if (row.tag == 'COBER.DET.DESC'):
                    dataRow.append(row.text)
                if (row.tag == 'COBER.DET.CAPITAL'):
                    dataRow.append(row.text)
                if (row.tag == 'COBER.DET.MONCAP'):
                    dataRow.append(row.text)
                if(row.tag == 'COBER.DET.MONPRI'):
                    dataRow.append(row.text)  
                if (row.tag == 'COBER.DET.PRMBRUTA'):
                    dataRow.append(row.text)
                if (row.tag == 'COBER.DET.LIMEDAD'):
                    dataRow.append(row.text)
                if (row.tag == 'COBER.DET.REGSVS'):
                    dataRow.append(row.text)
            
            if len(dataRow)>0:
                coberageList.append(dataRow)

        return coberageList

    def get_xml_to_dict(self):
        data = {}

        # Ruta del archivo XML
        archivo_xml = self.FILE_PATH

        # Lee el archivo XML with UTF-8 encoding
        tree = ET.parse(archivo_xml, parser=ET.XMLParser(encoding="utf-8"))
        root = tree.getroot()

        for element in root.iter():
            auxlabel = element.tag[element.tag.find('.') + 1:len(element.tag)]
            if(element.text and element.text != ""):
                data[auxlabel] = element.text
            else:
                data[auxlabel] = ""

        #print(json.dumps(data, indent=4, ensure_ascii=False).encode('utf-8').decode('utf-8'))
        return data