# Numbers - int
print("============ Numbers - int =============")
myint = 7
print(myint)
print()

# float
print("============ Numbers - float =============")
myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)
print()

# Strings
print("============ Strings =============")
mystring = 'hello'
print(mystring)
mystring = "hello double quotation"
print(mystring)
print()

# Strings with single qutation -> should use double quotation
print("============ Strings with single qutation =============")
mystring = "Don't worry about apostrophes"
print(mystring)
print()

# Simple operators can be executed on numbers and strings:
print("============ Simple operators with numbers and strings =============")
one = 1
two = 2
three = one + two
print(three)
print()

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)
print()

# Assignments can be done on more than one variable "simultaneously" on the same line like this:
print("============ simultaneously assign =============")
a, b = 3, 4
print(a, b)
print(a + b)

c, d = 7, 8
e, f = (c + a), (b + d)
print(e, f)

print("============  Mixing operators between numbers and strings (Not supported) =============")
one = 1
two = 2
three = 3.5
isBool = True
hello = "hello"
#print(one + two + hello) => You cannot do this.
print(str(one) + str(two) + str(three) + hello) # it works (converted all to String)

## type() function => if you want to confirm the type of variable.
print(type(one))
print(type(three))
print(type(hello))
print(type(isBool))

## how to verify if it's int or float......
if type(one) == int:
    print("The variable one is integer")

if isinstance(one, int): #=> This is more recommended.
    print("The variable one is integer (2)")


###########################################################
# But, you can print with String Formatting
# %s: String format specifier
# %d: Decimal (Integer) specifier
# %f: Floating-point specifier
###########################################################
print("one: %d, two: %d, three: %d, three-1: %f, hello = %s" % (one, two, three, three, hello))
print(f"one: {one}, two: {two}, three: {int(three)}, three-1: {three:.6f}, hello = {hello}") ## this is new style, more recommended.

mystring = 'hello'
myfloat = float(10)
myint = 20

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)