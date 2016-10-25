# Python

try:
	r = 3 / 10
except:
	print "Division entre 0"

try:
	6/0
except ZeroDivisionError as e:
	print "Error"

try:
	6/0
except Exception as e:
	print "%s" % e

try:
	6/0
except Exception as e:
	pass

try:
	6/0
except Exception as e:
	print "%s" % e
	raise e

# PHP

# try {
# 	$r = 3 / 10;
# } catch ( Exception $e ) {
# 	echo "Hoyo Negro";
# }