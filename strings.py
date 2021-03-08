# slicing
# mystring = abcd
# mystring[1:3] => bc
# mystring[::] whole thing
# mystring[::2] => ac
# optional thrid parameter is the step/jump size, allows you to skip values when return a slice dpeending on the size of teh step
# mystring[1:3:2] => b, becayse string doesnt include d, but with jump size being two, there is no where else to jum pto so just returns b
# start stop step size
# can reverse a string with mystring[::-1]


# immutability of stirngs
# doesn't support item reassignemnt if idenx within string etc 
# Strings are not mutable! (meaning you can't use indexing to change individual elements of a string)
# name = "Sam"
# # make Pam

# last_letters = name[1:]
# 'P' + last_letters
# concatenation


# string nums added together cocantenate rather than add


# strings have built in methods var.(list of methods populates) invoke them

# doesn't acutally infleunce the original verison of the string, or it is not in place methods
# would have to reassign the var to thh var with the method invoked

# .upper()/.lower()/.split()(based on white space or removes/splits at whatever ccharacter you input into paratheses)

# string formatting for printing etc


# interpolation - stick a variable in a string

# .format()
# new version:
# f-strings, formatted string literals

# print('This is a string {}'.format('INSERTED'))

# print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))

# or {f} {b}.format(f='fox', b='brown')



# float formatting
# setting the width/level of  precison for float number

print('The result was {r:width.precision f}'.format(r=result))

# widht value is amount of white space
# precison is number of decimals post  the deicmal point
# r:1.4f


# f-strings
print(f'Hello my name is {var_name}')



# formatting with placeholders
# %s can be used to onject string int your print statmens 
# a % is referred to in this cas as a stirng formatting operator

print("I'm going to inject %s here." %'something')

# can pass mutliple items this way using tuples
print("I'm going to inject %s text here, and %s text here." %('some', 'more'))
# can do the same by passing variable names into the typles as well, and will displayed in order
