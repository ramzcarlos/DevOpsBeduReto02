<<<<<<< HEAD
<<<<<<< .merge_file_oV5oFu
from BotonAtras import *
=======
from muestra import *
from BotonSiguiente import *
>>>>>>> .merge_file_3chdIu
=======
from BotonAtras import *
>>>>>>> features/BotonAtras
class Aplicacion():

	def main(self):
		# Imprimir en pantalla mensaje.
		print ("Hola Bedu! Esto Es Codigo en la Rama Principal")
		#llamando a funcion principal.

		inicioBotonAtras=BotonAtras()
		inicioBotonAtras.main()

		inicioMuestra=Muestra()
		inicioMuestra.main()
		InicioBotonSiguinete=BotonSiguiente()
		InicioBotonSiguinete.main()

		inicioBotonAtras=BotonAtras()
		inicioBotonAtras.main()


inicio=Aplicacion()	
inicio.main()