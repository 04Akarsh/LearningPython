#We can define variables using alphanumeric character and underscore _ only .
a=1
a_1=2
A=3


#Variables in python have DYNAMIC TYPING
print(type(a)) #will give out int
a="apple"
print(type(a)) #will output str , so we don't need to define type before changing variable value


#Shorthand operators can we used to remove repitative typing of variable 
x = 0
x = x + 1
x = x + 1
print(x)
#We can shorten the above code using shorthand operators , it works with every arithmatic operators

y = 0
y += 1
y += 1 #so y += 1 is same as x = x + 1
print(y)

#Membership Operators ( in , not in ) are used to check if particular value exists in something 

print("nintendo" in "fuck nintendo and their overpriced bs") #right wa , str in str

#print(12 in 345678) this is worng as we can check for int in int , only check for int in tuple

print(5 not in (1 ,2 ,3 ,4)) #right wasy coz i used a tuple as membership operator only checks for subset element 

#chaining operators , we can use multiple operators in a single logical statement

print(x > y > 10)
print(x == y == 2)
print(x * y == 4)
print(x // y == 0)


# ----------------------------------------------
# Escape Characters in Python - Examples
# ----------------------------------------------

# Newline (\n)
print("Hello\nWorld")   # Prints on two lines

# Tab (\t)
print("Name\tAge\tCity")      # Creates tab spaces between text
print("Alice\t21\tLondon")    # Tabs help align text like columns

# Single quote (\')
print('It\'s a sunny day')    # Allows single quote inside single-quoted string

# Double quote (\")
print("She said \"Hello\"")   # Allows double quotes inside double-quoted string

# Backslash (\\)
print("This is a backslash: \\")   # Prints a single backslash

# Carriage return (\r)
print("Hello\rWorld")   # 'World' overwrites 'Hello' → Output: World

# Backspace (\b)
print("Helloo\b")       # Removes the last 'o' → Output: Hello

# Form feed (\f)
print("Hello\fWorld")   # Page break (mostly visible in some editors)

# Bell (\a)
print("Bell sound\a")   # May produce a beep sound in some terminals

# Vertical tab (\v)
print("Hello\vWorld")   # Moves to a vertical tab position (similar to \n but different spacing)

# Octal value (\ooo)
print("\101")   # Octal 101 = 'A'

# Hex value (\xhh)
print("\x41")   # Hex 41 = 'A'

# Unicode by name (\N{name})
print("\N{GREEK CAPITAL LETTER DELTA}")   # Prints: Δ

# Unicode 16-bit (\uXXXX)
print("\u03A9")   # Greek Omega symbol Ω

# Unicode 32-bit (\UXXXXXXXX)
print("\U0001F600")   # 😀 (grinning face emoji)

# Raw strings (prefix r or R) - ignores escape sequences
print(r"C:\Users\John")   # Prints the backslashes as is

# Using expandtabs() to control tab size
text = "Name\tAge\tCity"
print(text.expandtabs(4))   # Converts tabs to 4 spaces each
