import math
n=list(map(int,input().split(",")))
l=len(n)
w=[]
for i in range(l):
    s=0
    sq=math.sqrt(n[i])
    if sq.is_integer():
        s+=5
    if n[i]%4==0 and n[i]%6==0:
        s+=4
    if n[i]%2==0:
        s+=3
    w.append(s) 
wei={}     
for i in range(l):
    num=n[i]
    weight=w[i]
    wei[num]=weight
sorted_dict=sorted(wei.items(),key=lambda x:x[1])
print(sorted_dict)
