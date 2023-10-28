f=open('a.txt','r')
l=list()
for s in f:
    l.append(s)
f.close()
print(l)