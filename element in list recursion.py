l = [1,2,3,4,6,7,8,9]
num = 0
n = 0

#My version which i wrote myself , uses less memory but less easy to understand 
def find(l,num,n):
    if not l:
        return False
    if n >= len(l):
        return False
    if l[n] == num:
        return True
    else: 
        n += 1
        return find(l,num,n)

print(find(l,num,n))

#Gemini version 
def find_recursive(my_list, target):
    # BASE CASE 1: If the list is empty, the target definitely isn't there
    if not my_list:
        return False
    
    # BASE CASE 2: If the first item is the target, we found it!
    if my_list[0] == target:
        return True
    
    # THE RECURSION: Search the REST of the list (everything from index 1 onwards)
    return find_recursive(my_list[1:], target)

print(find_recursive(l,num)) # Returns True