class Auto:
	name = ""
	kind = ""
	color = ""
	value = 100.320545
	_numero_serie = ""
	def description(self):
		desc = "%s es un %s %s. Vale $%.2f" % (self.name, self.color, self.kind, self.value)
		return desc

car1 = Auto()
car1.name = "Nombre"
car1.color = "Rojo"
car1.value = 34323.32423434215

print car1.description();

# Otro Ejemplo

class MiClase:
    variable = "hola"

    def function(self):
        print "Este es un mensaje."

myobjectx = MiClase()
myobjectx.variable

# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# your code goes here
car1 = Vehicle()
car1.name = "Nombre"
car1.color = "Rojo"
car1.value = 100000

# test code
print car1.description()