"""
[summary]
"""

# strings are used to represent text
# by default it's unicode text in python 3 and ascii in python 2

name = 'hiroyuki'
language = "日本語"
place = """日本"""

"hello".capitalize()
"hello".replace("e", "a")  # First character denotes character to replace
"hello".isalpha()  # == True //
"123".isdigit()  # == True //  Useful when converting to int

# splitting a series of characters into a list
'some,csv,values'.split(',')  # == ['some', 'csv', 'values']

# Printing quotations using backslash
print("\"神様になった日\"")

# Printing normal backslash
print("Σ/神様になった日")

# String concatenation
phrase = "\'神様になった日"
print(phrase + "がかっこいい")

# String concatenation long method
phrase = "神様になった日"
feeling =  "がかっこいい"
full = f"{phrase}{feeling}"
print(full)

phrase = " Apple is tasty"
# Makes a string entirely upper case
print(phrase.upper())

# Makes a string entirely lower case
print(phrase.lower())

# Capitalizes the first word
print(phrase.capitalize())

# Capitalizes the first letter of every word
print(phrase.title())

# Strips out any white spacing from the string
print(phrase.strip())

# Strips out any white spacing from the left side of the string
print(phrase.lstrip())

# Strips out any white spacing from the right side of the string
print(phrase.rstrip())

# Find the index of the first given character or sequence of characters in the string
print(phrase.find("be"))

# Replaces the index of the first given character or sequence of characters in the string
print(phrase.replace("tasty", "healthy"))

# Finds the given character or sequences of characters in a given string. Returns a boole value
print("Apple" in phrase)

# Returns a boole value whether the supplied character or sequence of characters exists inside a given  string
print("Apple" not in phrase)

# Returns a boole if a string is entirely in the upper case or not
print(phrase.isupper())

# Returns a boole if a string is entirely in the lower case or not
print(phrase.islower())

# Makes a string entirely lower case then returns a boole whether a string is entirely in the upper case or not
print(phrase.upper().isupper())

# Printing the length of a string/how many characters
phrase = "\"神様になった日\""
print(len(phrase))

# Prints out the value/character based on the assigned index
phrase = "\"神様になった日\""
print(phrase[1])

# Returns the index value of the given supplied character
phrase = "\"神様になった日\""
print(phrase.index("日\""))

# Replaces an existing value with a different one. Takes two arguments, first bring the target & second being the target value
phrase = "\"神様になった日\""
print(phrase.replace("日", "月"))

#  Adding a double quote inside a string
phrase ="Python \"Programming"
print  (phrase)

#  Adding a single quote inside a string
phrase ="Python \'Programming"
print  (phrase)

#  Adding a double slash inside a string
phrase ="Python \\\\ Programming"
print  (phrase)

# Printing quotations using backslash
print("\"神様になった日\"")

# Printing normal backslash
print("Σ/神様になった日")
