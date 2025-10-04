#Creating ceaser ciper

alpha="abcdefghijklmnopqrstuvwxyz"
a="halicaliz"
#now if i want to get my output as halicali but shifted by k num of letters , without loops

new_cipher = ""

i=0 #idk why i initialised this variable if i'm always gonna start from 0 index and not using loops lol
k=20 #this is used to control how much shift i want in my output 

new_cipher+= (alpha[(((alpha.index(a[i]))+k)%26)]) #we first find the value at 0 in var a
new_cipher+= (alpha[(((alpha.index(a[i+1]))+k)%26)]) #then we take that value and find it's index in aplha
new_cipher+= (alpha[(((alpha.index(a[i+2]))+k)%26)]) #then we take that index and add 1 
new_cipher+= (alpha[(((alpha.index(a[i+3]))+k)%26)]) #then we find the value at resultant index
new_cipher+= (alpha[(((alpha.index(a[i+4]))+k)%26)]) #then we % by 26 as if the resultand became more than 25 it will cause out of range error 
new_cipher+= (alpha[(((alpha.index(a[i+5]))+k)%26)]) #modding by 26 fixes that issues coz if the resultant is smaller than 26 it stays the same
new_cipher+= (alpha[(((alpha.index(a[i+6]))+k)%26)]) #but if its equal or bigger than 26 it's starts over from index 0 as 26 % 26 = 0
new_cipher+= (alpha[(((alpha.index(a[i+7]))+k)%26)])
new_cipher+= (alpha[(((alpha.index(a[i+8]))+k)%26)])

print(new_cipher)