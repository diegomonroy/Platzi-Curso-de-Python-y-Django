# If

# Python

nombre = "Diego"
if nombre == "Diego":
	nombre = "Diego Monroy"
elif nombre == "YouTube":
	nombre = "Hola YouTube"
else:
	nombre = "Quién eres?"

# PHP

# $nombre = "Diego";
# if ( $nombre == "Diego" ) {
# 	$nombre = "Diego Monroy";
# } else if ( $nombre == "YouTube" ) {
# 	$nombre = "Hola YouTube";
# } else {
# 	$nombre = "Quien eres?";
# }

# While

# Python

contador = 0
while contador < 5:
	print "numero %i" % contador
	contador += 1

# PHP

# $count = 0;
# while ( $count < 5 ) {
# 	echo "Number" . $count;
# 	$count += 1;
# }

# For

# Python

for i in range(4):
	print "Numero %i" % i

range(1, 6)

range(0, 11, 5)

for i in "Hola Mundo":
	print "%s" %i

# PHP

# for ( $i = 0; $i < 5; $i++ ) {
# 	echo "Numero" . $i;
# }

# Tabulación

class Estudiante(object)
	def __init__(self, nombre, edad):
		self.nombre = nombre
		self.edad = edad

	def hola(self):
		if self.edad > 18:
			return '%s es mayor' % self.nombre
		else:
			return '%s es menor' % self.nombre