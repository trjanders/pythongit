#! /usr/bin/python
# textmenu.py version 1.0 

# python for Windows peculiarities and customizations https://docs.python.org/3.3/using/windows.html

# on windows set path to include pythonpath and set to c:\path\to\pythonversion
# file association on windows 'assoc .py=Python.File'
# run .pyw scripts without terminal window popping 'ftype Python.File=C:\Local\Python34\pythonw.exe "%1" %*'

# or run from command line using 'py scriptname.py'


#build text menu
print(17 * '.')
print("Do you want to play a game?")
print("  How bout global thermo ... er ... How bout Calculator?")
num1 = raw_input(' Give me a number: ')
num2 = raw_input(' Give me another number: ')
print("  1. Add")
print("  2. Subtract")
print("  3. Multiply")
print("  4. Divide")
print(17 * '.')
print(13 * ' . ')
menuItem = raw_input(' Make a Selection: ')

#cast variables as float or int
num1 = float(num1)
num2 = float(num2)
menuItem = int(menuItem)

#todo##############################
#do the expected actions
if menuItem == 1:
	answerAdd = float(num1)+float(num2)
	#print answer
	print('{0} + {1} is {2}'.format(num1,num2,answerAdd))
elif menuItem == 2:
	answerSubtract = float(num1)-float(num2)
	print('{0} - {1} is {2}'.format(num1,num2,answerSubtract))
elif menuItem == 3:
	answerMultiply = float(num1)*float(num2)
	print('{0} x {1} is {2}'.format(num1,num2,answerMultipl7))
elif menuItem == 4:
	if num2 == (0 || 0.0 || 0.00)    #avoid dividing by 0
	print("cmon man. exiting on 0.")
	else ## default choice
		answerDivide = float(num1)/float(num2)
		print('{0} / {1} is {2}'.format(num1,num2,answerDivide))
else: ##default choice
	print("Make a Selection by typing one of the following choices 1, 2, 3 or 4.  Try again. ")
	
	
