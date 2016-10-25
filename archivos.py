import string
import random




fo = open("foo.txt","wb")
fo.write("Python es el mejor lenguaje.\nEs genial!!\n")
for i in range(1000):
    texto = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(10))
    fo.write("%s\n" % texto)
fo.close()

fo2 = open("foo.txt","r+")
srti = fo2.read()
print srti
fo2.close()