"""
a = "Hola"
b = "Mundo"
c = "!"
""""

#print a,b,c

def mi_funcion():
    return "Esta es mi primera funcion"

def mi_funcion_2():
    print "Este es otro tipo de funcion"

resultado = mi_funcion()
print resultado

mi_funcion_2()

def suma( a1, b1 ):
    return a1 + b1

resultado_2 = suma( 10, 5 )
print resultado_2

def saludo( nombre ):
    return "Hola %s" % nombre

print saludo( "Diego" )