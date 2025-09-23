#how to take input 

n=str(input("Input your name :"))
p=int(input("input  your age :"))
print(f"Hello {n} nice to meet you , good to know you're {p} years old now ")
print("in 20 years you will be" , p + 20 , "years old although you're already so old fat and ugly you should probably kill yourself")
c=int(input("Now i'm gonna tell you the ares of a circle , tell me its radius :"))
print("The area of this circle is" , 3.14 * c * c )

#how to display data types for multiple variables using a list 

L=[n,p,c]
types= [type(var) for var in L]
print(types)

#using values of list to display values

print(L[0])
print(L[2])

#how to display data type of some element of a list

print(type(L[2]))

#hhh

dob = input("day:" , "month:" , "year:")
print(dob)