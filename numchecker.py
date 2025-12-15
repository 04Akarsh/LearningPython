'''BIG ASS METHOD
f = open("num.txt", "r")

while True:
    s=f.readline()
    if not s:
        print("He aint here bro")
        break
    n=int(s.strip())
    if (n==72):
        print("yayyy it's here !")
        break
f.close()'''
#METHOD WITHOUT WHILE AND WITHOUT FLAG
with open('num.txt','r') as f:
    for line in f:
        s = int(line.strip())
        if s == 1321312:
            print("yayyy it's here !")
            break
    else:
        print("He aint here bro")

#METHOD WITH FLAG   
'''
flag = False
with open('num.txt','r') as f:
    for line in f:
        s = int(line.strip())
        if s == 1321312:
            print("yayyy it's here !")
            flag = True
            break
if flag == True:
    print('He aint here bro')'''