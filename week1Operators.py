#Types of operators in Python
# 1) Arithmetic operators (+ , - , * , / , % , // , **)
print("ARITHMATIC OPERATORS")
print("\nAddition 5 + 7 =" , 5+7 , "(It's also used for Concatination)") 
print("Subtraction 5 - 7 =", 5-7 )
print("Multiplication 5 * 7 = ", 5 * 7)
print("Division 5 / 7 =" , 5 / 7 , "(It will always return float value)")
print("Floor division 5 // 7 =" , 5 //7 , "(It always returns int values)")
print("Modulus 5 % 7 =", 5 % 7 ,"(Always returns the remainder in division)")
print("Modulus 7 % 5 =" , 7 % 5 )
print("Exponentiation 5 ** 7 =" ,  5**7 , "(5 to the power of 7)" )

print("\n-------------")
# 2) Realtional operators (> , < , >= , <= , == , !=)
print("\nRELATIONAL OPERATORS")
print("\nis 5 > 7 ?" , 5 > 7 )
print("is 5 < 7 ?", 5 < 7)
print("is 5 equal to or less than 7 ?" , 5 <= 7)
print("is 5 equal to or more than 7 ?" , 5 >= 7)
print("is 5 equal to 7 ?", 5 == 7)
print("is 5 not equal to 7 ?" , 5 != 7)
print("\n-------------")
# 3) Logical operators (and , or , not)

print("\nLogical operators :")
print("\nAND operator returns true only if all cases are true , \nfor ex : 5 > 7 and 7 > 5 is" , 5>7 and 5<7)
print("OR returns true if atleast one case is true , for ex: 5 > 7 or 7 > 5 is " , 5>7 or 7>5)
print("NOT inverts a boolean value , for ex : not 5 > 7 is" , not 5 >7 , "(Not can be used with or without () like not (5>7) is same as not 5>7)")



# Python Operator Precedence (Highest to Lowest)

# 1. Parentheses
#    ()
#    Used to group expressions and override precedence

# 2. Exponentiation
#    **
#    Right-to-left associativity

# 3. Unary plus, minus, bitwise NOT
#    +x, -x, ~x

# 4. Multiplication, Division, Floor Division, Modulus
#    *, /, //, %

# 5. Addition and Subtraction
#    +, -

# 6. Bitwise Shift Operators
#    <<, >>

# 7. Bitwise AND
#    &

# 8. Bitwise XOR
#    ^

# 9. Bitwise OR
#    |

# 10. Comparison Operators
#     ==, !=, >, >=, <, <=, is, is not, in, not in

# 11. Logical NOT
#     not

# 12. Logical AND
#     and

# 13. Logical OR
#     or

# 14. Conditional Expression
#     x if condition else y

# 15. Assignment Operators
#     =, +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<=

# 16. Lambda Expression
#     lambda arguments: expression
