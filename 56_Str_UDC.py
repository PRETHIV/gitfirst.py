# Hello World program in Python
#guvi this is rocky
x,y=map(str,input().split(" "))
lx=len(x)
ly=len(y)
c=0
if ly>lx:
    n=ly-lx
    for i in range(n):
        x+=" "
elif lx>ly:
    e=""
    for i in range(ly):
        e+=x[i]
    x=e
    c=c+(lx-ly)
for i in range(len(x)):
    if x[i]!=y[i]:
        c+=1
print(c)
