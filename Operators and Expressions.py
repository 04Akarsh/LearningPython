# #Types of Operators in integers and float
# Following is the operator precedence in Python:
# Operators	Meaning
# ()	Parentheses
# **	Exponent
# +x, -x, ~x	Unary plus, Unary minus, Bitwise NOT
# *, /, //, %	Multiplication, Division, Floor division, Modulus
# +, -	Addition, Subtraction
# <<, >>	Bitwise shift operators
# &	Bitwise AND
# ^	Bitwise XOR
# |	Bitwise OR
# ==, !=, >, >=, <, <=, is, is not, in, not in	Comparisons, Identity, Membership operators
# not	Logical NOT
# and	Logical AND
# or	Logical OR

# Notes:
# 1. 10 * 2 / 5 --> here * and / are of same precedence in such case the precedence takes place from left to right. eg: 10 * 2 / 5 --> 4.0 and 10 / 2 * 5 --> 25.0
# 2. when a = 10, b = 5 then a//b --> 10//5 --> 2  a%b --> 10%5 --> 0 (reminder)
# 3. when a = 5, b = 10 then a//b --> 5//10 --> 0  a%b --> 5%10 --> 5 (numerator). therefore in modulo division when numerator is less than that of denominator numerator % denominator == numerator value."""
print("Taking int and float variables and performing basic operations on them")
n = 1
m = 1
l = 1.2
p = 3
o = 9.6
j = 9.6
k = 9.6

print(f"n = {n} \nm = {m} \nl = {l} \np = {p} \no = {o} \nj ={j}")

n = n + 2
m = m * 2
l = l * 2.1
p = p ** 2
o = o / 2
j = j // 2 #Floor division remove the decimal part
k = k % 2 #modulus operator gives out the remainder

print(f"n + 2 is {n} \nm * 2 is {m} \nl * 2.1 is {l} \np square is {p} \no's division by 2 is {o} \nj floor division by 2 is {j} \nk mod 2 is {k}")

print("Now taking string variables but we can only perform additon on them AKA CONCATINATION")
q = "qwerty"
a = "asd"
print("When we add qwerty and asd we just put the strings together =" , q+a)
first_name = "Aka"
last_name = "vas"
print("But what if we needed sapce between them ? \nThen we add space between them simple . So Aka + vas would be\n" + first_name + " " + last_name)

list_1 = [1,2,3]
list_2 = [2,3,4]
print(f"CONCATINATION works same for lists too for ex: list1 + list 2 is\n{list_1 + list_2}")