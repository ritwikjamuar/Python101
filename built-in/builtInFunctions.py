#****************************************************** abs ( x ) ******************************************************

print ( '******************************************* Method : abs ( x ) *******************************************\n' )

''' Return the absolute value of a number. The argument may be an integer or a floating point number.
	If the argument is a complex number, its magnitude is returned. '''

print ( abs ( 3 ) )
print ( abs ( -2 ) )
print ( abs ( -7.5 ) )
print ( abs ( 2 + 3j ) )

print ( '\n' )

#****************************************************** all ( x ) ******************************************************

print ( '******************************************* Method : all ( x ) *******************************************\n' )

''' Return True if all elements of the iterable are true ( or if the iterable is empty ).
	Equivalent to:

	def all ( iterable ) :
		for element in iterable :
			if not element :
				return False
		return True
'''

print ( all ( "Reservoir" ) )

print ( '\n' )

#****************************************************** any ( x ) ******************************************************

print ( '******************************************* Method : any ( x ) *******************************************\n' )

''' Return True if any element of the iterable is true.
	If the iterable is empty, return False.
	Equivalent to:

	def any ( iterable ) :
		for element in iterable :
			if element :
				return True
		return False
'''
array = [ 1, 2, 3, 4, 'n' ]
print ( any ( array ) )

print ( '\n' )

#***************************************************** ascii ( x ) *****************************************************

print ( '***************************************** Method : ascii ( x ) *******************************************\n' )

''' As repr (), return a string containing a printable representation of an object,
	but escape the non-ASCII characters in the string returned by repr () using \\x, \\u or \\U escapes.
	This generates a string similar to that returned by repr () in Python 2.'''

print ( ascii ( array ) )

print ( '\n' )

#****************************************************** repr ( x ) *****************************************************

print ( '****************************************** Method : repr ( x ) *******************************************\n' )

''' Return a string containing a printable representation of an object.
	For many types, this function makes an attempt to return a string
	that would yield an object with the same value when passed to eval (),
	otherwise the representation is a string enclosed in angle brackets
	that contains the name of the type of the object
	together with additional information
	often including the name and address of the object.
	A class can control what this function returns for its instances by defining a __repr__() method.'''

x = 'Halo'
print ( repr ( x ) )
print ( x.__repr__() )

# Consider this example :

class Bike :
	def __init__ ( self, volume, power, torque ) :
		self.volume = volume
		self.power = power
		self.torque = torque

ninjaH2 = Bike ( 1000, 326, 297 )

# When a object of a class has been given as argument to print () method, it will print Memory Address of Object.
print ( ninjaH2 )

# However, through object, values of members of class is accessible.
print ( ninjaH2.volume, ninjaH2.power, ninjaH2.torque )

# In order to print a formatted text when an object is printed using print () method,
# override '__str__ ( self )' method and return a string you wish.
# Consider this example :

class Car :
	def __init__ ( self, volume, power, torque ) :
		self.volume = volume
		self.power = power
		self.torque = torque
	
	def __str__ ( self ) :
		return 'Car:\nVolume : {self.volume}\nPower : {self.power}\nTorque : {self.torque}'.format ( self = self )

aventador = Car ( 6536, 700, 592 )

# What print method does to an object is that it calls '__str__ ( self )' method of that object.
# Same can be observed with 'str ( string )'.
# If this method is not defined for the class, then 'print ()' will just print the address of object on the memory.
print ( aventador )

# However, if you just use object in interpreter, the interpreter will return memory address of object,
# even though class has '__str__ ( self )' method overridden.
# This is because, interpreter will call '__repr__ ( self )' method of class's object.

class Truck :
	def __init__ ( self, payLoad, distance ) :
		self.payload = payLoad
		self.distance = distance
	
	def __str__ ( self ) :
		return '__str__ of Truck'
	
	def __repr__ ( self ) :
		return '__repr__ of Truck'

volvo500 = Truck ( 5000, 200 )

# 'print ()' or 'str ()' will call '__str__ ( self )' method of class the object belongs to.
print ( volvo500 )

# If 'repr ()' is used with object given as parameter,
# the '__repr__ ( self )' method of class the object belongs to, is called.
print ( repr ( volvo500 ) )

# Best way to use '__repr__ ( self )' : Return the vaild python call that shows actual parameter
# passed to the constructor of object.
# For example :

class Cycle :
	def __init__ ( self, distance ) :
		self.distance = distance
		self.className = self.__class__.__name__
	
	def __str__ ( self ):
		return 'Cycle :\ndistance : {self.distance} \n'.format ( self = self )
	
	def __repr__ ( self ) :
		return '{self.className} ( {self.distance} )'.format ( self = self )

bmx = Cycle ( 50 )

print ( bmx )

print ( repr ( bmx ) )

print ( '\n' )

#********************************** eval ( expression, globals = None, locals = None ) *********************************

print ( '********************** Method : eval ( expression, globals = None, locals = None ) ***********************\n' )

''' The arguments are a string and optional globals and locals.
	If provided, globals must be a dictionary.
	If provided, locals can be any mapping object.
	
	The expression argument is parsed and evaluated as a Python expression ( technically speaking, a condition list )
	using the globals and locals dictionaries as global and local namespace.
	
	If the globals dictionary is present and lacks ‘__builtins__’,
	the current globals are copied into globals before expression is parsed.
	
	This means that expression normally has full access to the standard builtins
	module and restricted environments are propagated.
	
	If the locals dictionary is omitted it defaults to the globals dictionary.
	If both dictionaries are omitted, the expression is executed in the environment where eval () is called.
	The return value is the result of the evaluated expression.
	Syntax errors are reported as exceptions.
	Example :

	>>> x = 1
	>>> eval ( 'x+1' )
	2
	
	This function can also be used to execute arbitrary code objects (such as those created by compile () ).
	In this case pass a code object instead of a string.
	If the code object has been compiled with 'exec' as the mode argument, eval ()’s return value will be None.
	
	Hints : dynamic execution of statements is supported by the exec () function.
			The globals () and locals () functions returns the current global and local dictionary,
			respectively, which may be useful to pass around for use by eval () or exec ().
			See ast.literal_eval () for a function that can safely evaluate strings with expressions containing
			only literals.'''

num = 2
print ( eval ( 'num' ) )
print ( eval ( 'num ** 3' ) )
print ( eval ( 'num == 1' ) )
print ( eval ( 'all ( x )' ) )

# The purpose of 'eval' is to evaluate an expression, not a definition.
# If you try to evaluate an definition, then there would be Syntax Error raised by Python Interpreter.
# Also, eval will return resultant object of expression.
# Try running this script with str () method call removed.
x = input ( 'Enter some Expression\n' )
print ( '\n' + str ( eval ( x ) ) + '\n' )

