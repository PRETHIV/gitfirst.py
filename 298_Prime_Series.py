#N_Prime_Nos
def chkpr(no):
    if no<2:
        return False
    else:
        p=True
        for i in range(2,no):
            if no%i==0:
                p=False
                break
        return p
n=int(input())
l=[]
for i in range(n):
    if chkpr(i):
        l.append(i)
    else:
        continue
for i in range(len(l)):
    if i==len(l)-1:
        print(l[i],end="")
    else:
        print(l[i],end=" ")
