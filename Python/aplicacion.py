from muestra import *
from BotonInicio import *
class Aplicacion():

	def main(self):
		# Imprimir en pantalla mensaje.
		print ("Hola Bedu! Esto Es Codigo en la Rama Principal")
		#llamando a funcion principal.
		inicioMuestra=Muestra()
		inicioMuestra.main()
		inicioBotonIncio=BotonInicio()
		inicioBotonIncio.main()

inicio=Aplicacion()	
inicio.main()