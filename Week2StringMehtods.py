#Note: All string methods returns new values. They do not change the original string.
a="Hornet is in silksong"
b="    The one piece is real****"

print(a.lower())         #Returns all char in lower case
print(a.upper())         #Returna all char in upper case
print(a.capitalize())    #Upper cases the first char
print(a.title())         #turns first letter of every word to upper case
print(a.swapcase())      #swaps all lower case for upper case , vice versa
print(a.center(30))      #Returns a centered string
print(a.count("Hornet")) #Returns the number of times a specified values occurs in string (case sensitive)
print(a.count("hornet")) #Returns the number of times a specified values occurs in string (case sensitive)
print(b.strip())         #The strip() method removes any leading, and trailing whitespaces.
print(b.strip("-"))      #You can specify which character(s) to remove, if not, any whitespaces will be removed
print(b.lstrip())        #The lstrip() method removes any leading characters (space is the default leading character to remove)
print(b.rstrip("*"))     #The rstrip() method removes any trailing characters (characters at the end a string), space is the default trailing character to remove.
print(a.count("i"))      #Returns how many specified values are in the string 
print(a.index("i"))      #Searches for the FIRST OCCURANCE of specified value and returns it 
print(a.replace("i", "h")) #replaces every specified value with another value

#String methods with logic

print(a.islower())          #Returns true if all char are lower
print(a.isupper())          #Returns true if all char are upper)
print(a.istitle())          #Returns true if first char of every word is upper
print(a.isdigit())          #Returns true if all char in string are digit (not int but digit)
print(a.isalpha())          #Returns true if all char are alphabets (non numeric)
print(a.isalnum())          #Returns true if ll char in string are alpha-numeric
print(a.startswith("H"))    #Returns true if it starts with the specified value 
print(a.endswith("p"))      #Returns true if ends with specified value
