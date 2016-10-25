class Persona:
	def saludo_general(self):
		return "Hola Persona"

class Estudiante(Persona):					#Hereda de object, siempre se nombra con mayuscula
	def __init__(self, nombre, edad):		#Es el cosntructor, self se usa siempre en clases
		
		self.nombre = nombre
		self.edad = edad
	def hola(self):							#Es la funcion que contiene nuestra clase Estudiante
		return "Mi nombre es %s\n" % self.nombre

e = Estudiante("Arturo",21)				 	#Asi creamos un objeto de la clase Estudiante
print e.saludo_general()
e1 = Estudiante("Fabian",21)
e2 = Estudiante("Pablo",21)
print e.hola(), e1.hola(), e2.hola();