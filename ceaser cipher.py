'''so what were gonna do is make a ceaser cipher in which the letters of alphabets are 
shifted by some arbitary number like 3 so a becomes , b becomes e .... and so on '''
import string
def create_CeaserCipher():
    l=string.ascii_lowercase #make a string of lowercase alphabet
    l=list(l)                #convert it to a list
    d={}                     #make a empty dict
    for i in range(len(l)):  #runs code from a to z(length of l list)
        d[l[i]]=l[(i+3)%26]  #takes the alphabet as key , ads 3 to it and mods by 26 so x can become a , and assigns it to the key
    return d                 #dicdicdic

d=create_CeaserCipher()
with open('sherlock.txt' , 'r') as f:
    with open('encrypted_sherlock.txt','w') as g:
        c = f.read(1)
        while c!='':
            g.write(d.get(c, c))
            c = f.read(1)
with open('encrypted_sherlock.txt', 'r') as result_file:
    print(result_file.read())