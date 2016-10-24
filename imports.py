>>> import datetime
>>> dir( datetime )
>>> datetime.date.today()
>>> datetime.datetime.now()

>>> from datetime import datetime
>>> from datetime import datetime, date
>>> date.today()
>>> datetime.now()

>>> from datetime import datetime, date, timedelta
>>> timedelta(microseconds=1)

# Factorial

# 5!
>>> 5*4*3*2*1

factorial = 5
acum = 1
while factorial>0:
	acum = acum * factorial
	factorial = factorial - 1
	print "%i" % acum
print "Resulrado : %i" % acum

# Recursion

def factorial(x):
	if x == 0:
		return 1
	else:
		return x * factorial( x - 1 )

print factorial(5)