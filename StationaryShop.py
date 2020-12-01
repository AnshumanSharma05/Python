'''
A new stationary shop has been opened in the city. The owner asks his accountant to take the list of items sold in the store. The list should contain the details of the items and their costs. Help the accountant to generate the prince list by writing a Python program.  Generate list with just 4 products -  A4sheets, pen, pencil and eraser and get the price of the items from the user.  Please refer the sample input and output statements for more clarifications.

Note:

The amount must be displayed with 2 decimal places. 
On entering the product price to be a negative number, the program should display the message " Invalid input" and stop the program. 


Sample input 1 :

Cost of A4sheet:

40

Cost of pen:

20

Cost of pencil:

10

Cost of eraser:

5
'''

cs=float(input("Cost of A4sheet:"))
if(cs<0):
	print("Invalid input")
	exit()
cp=float(input("Cost of pen:"))
if(cp<0):
	print("Invalid input")
	exit()
cpe=float(input("Cost of pencil:"))
if(cpe<0):
	print("Invalid input")
	exit()
ce=float(input("Cost of eraser:"))
if(ce<0):
	print("Invalid input")
	exit()
print("Items Details")
print("A4sheet:%0.2f"%cs)
print("Pen:%0.2f"%cp)
print("Pencil:%0.2f"%cpe)
print("Eraser:%0.2f"%ce)

