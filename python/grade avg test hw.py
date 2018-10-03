muffin = 20
cupcake = 20
sale = 1
while sale != 0:
	sale = input("")
	if sale == 'muffin':
		muffin -= 1
	elif sale == "cupcake":
		cupcake -= 1
	elif sale == 0:
		print( 'muffins: ' , muffin , "cupcakes: " , cupcake) 
if muffin == 0:
	print("Out of stock")
if cupcake == 0:
	print( "Out of stock")
