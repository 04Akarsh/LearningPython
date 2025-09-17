#types of data 
a = 1
b = "s"
c = 7.24
d = True

list_l= [ a , b , c,d]

#printing types of data
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(list_l))

##how to change data types

a = float(a)
c = str(c)

print("a's type was int now it is " , type(a))
print(c , type(c))

#but if we convert float to int it will lose decimal value

e = 2.31
e = int(e)
print(e , type(e))

#Boolean is special , its always true expect at 0
j = bool(10)
k = bool(0)
l = bool(-72.45)
m = bool("coco")
n = bool("")
print(j , type(j))
print(k , type(k))
print(l , type(l))
print(m , type(m))
print(n , type(n))