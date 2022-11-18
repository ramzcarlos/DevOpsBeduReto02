from muestra import *
from BotonSiguiente import *
class Aplicacion():

	def main(self):
		# Imprimir en pantalla mensaje.
		print ("Hola Bedu! Esto Es Codigo en la Rama Principal")
		#llamando a funcion principal.
		inicioMuestra=Muestra()
		inicioMuestra.main()
		InicioBotonSiguinete=BotonSiguiente()
		InicioBotonSiguinete.main()

inicio=Aplicacion()	
inicio.main()