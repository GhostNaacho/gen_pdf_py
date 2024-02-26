import sys
from generacion_pdf.pdf_module import PDF

#CRETAED AND MANTAINED BY GHOST - IGNACIO RIQUELME LAST UPDATE: 26-FEB-2024. 
def main():
    try:
        #Get args passed into the execution of script.
        arg0 = str(sys.argv[0]) 
        arg1 = str(sys.argv[1])

        #Print args.
        i=0
        for arg in sys.argv:
            print(f"arg[{i}] - {arg}")
            i+=1

        # Instantiation pdf class
        pdf = PDF(format='letter')
        pdf.set_font("helvetica", size=12)

        # Call pdf function to generate custom pdf. 
        pdf.gen_pdf_vida(arg1)

    except Exception as ex:
        print('Excepcion !',str(ex))

if (__name__ == "__main__"):
    main()