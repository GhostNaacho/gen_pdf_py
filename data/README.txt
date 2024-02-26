CRETAED AND MANTAINED BY GHOST - IGNACIO RIQUELME LAST UPDATE: 26-FEB-2024. 

CONDICIONES PARTICULARES DE LA POLIZA ACCIDENTES PERSONALES

BCI Seguros Vida S.A., en consideración a la Propuesta de Seguro presentada por 
el contratante y/o asegurado, suDeclaración de Salud si corresponde, las 
Condiciones Generales respectivas y las Condiciones Particulares que a 
continuación se detallan, acepta por medio de la presente póliza en asegurar 
lo siguiente:
__________________________________________________________________________________
|SUCURSAL : TELEMARKETING | PROPUESTA N°: 200124862 | PÓLIZA N°: AP / 466258 / 10 |
|_________________________________________________________________________________|
|                                                                                 |  
|CONTRATANTE                                                                      |
|_________________________________________________________________________________|
|Nombre 	  : JOSE BERNARDO GONZALES VARGAS RUT : 6178395-4                     |
|Dirección : ELEODORO RODRIGUEZ MATE 0376 NRO                                     |
|Comuna 	  : MAIPU Ciudad : SANTIAGO                                           |
|Teléfono  : E-Mail :                                                             |
|_________________________________________________________________________________|
|ASEGURADO TITULAR                                                                | 
|Nombre    : JOSE BERNARDO GONZALES VARGAS 						RUT : 6178395-4   |
|Dirección : ELEODORO RODRIGUEZ MATE 0376 				        NRO :             | 
|Comuna    : MAIPU 										     Ciudad : SANTIAGO    |
|Teléfono  : 									Fecha de Nacimiento : 25/03/1949  |
|_________________________________________________________________________________|
|VIGENCIA DEL SEGURO                                                              |
|_________________________________________________________________________________|
|Desde : 29/10/2022 								Hasta : 28/10/2023            |
|_________________________________________________________________________________|
|                                                                                 |
|PLAN, COBERTURAS Y PRIMA                                                         |
|_________________________________________________________________________________|
|Plan : PLAN 1.1 AÑOS DORADOS F TITULAR                                           |
|_________________________________________________________________________________|
|                                                                                 |
|Coberturas 	Capital Asegurado PrimaBruta Mensual Límite de Edad Registro C.M.F|
|                                                                                 |
|MUERTE ACCIDENTAL UF 50,0000 UF 0,0952 80 AÑOS POL320130409 -                    |
|                 	  															  |
|FRACTURA POR ACCIDENTE UF 12,0000 UF 0,0948 80 AÑOS POL302046 -                  |
|                  																  | 
|DESCUENTO FARMACIA UF 0,0000 UF 0,0000 80 AÑOS -                                 |
|	                                                                              |
|SERVICIO DE ORIENTACION MEDICA UF 0,0000 UF 0,0000 80 AÑOS                       |
|_________________________________________________________________________________|
|																				  |
|Primas Totales : Exenta UF 0,0952 		Afecta UF 0,0797                          |
|					IVA UF 0,0151 		Bruta  UF 0,1900                          | 
|_________________________________________________________________________________|
|							PAGO DE PRIMAS                                        |
|							Periodicidad de Pago : MENSUAL                        |
|							Forma de Pago        : MULTI-TIENDA                   |
|							Día de Pago          : 2 DE CADA MES                  |
|_________________________________________________________________________________|
|							CORREDOR :                                            |
|							R.U.T    : 76.726.150 - 0                             |
|							Nombre   : VOLVEK CORREDORES DE SEGUROS S.A.          |  
|							Comisión del Corredor : 0,000 % DE LA PRIMA NETA      |
|																				  |	
|																				  |	
|BCI SEGUROS VIDA S.A. Fecha de Emisión : 05/09/2022                              |
|_________________________________________________________________________________|


1.-create module xml_module.py
    - read data bulk to dict
    - read coverages bulk to array inside array

2.-create module barcode_module.py
    - generate a barcode with given value iside of class instantiation, importig barcode as png format in project folder.

3.-create module pdf_module.py
    - bussines logic to create pdf and import to unify modules to get final output pdf:
        * import xml_module
        * import barcode_module
        * create and call main function to unify tasks.
