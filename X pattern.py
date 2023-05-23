n=int(input())
s=input() 
for a in range(n):
    b=n-1-a
    #print(j,end=" ")
    for c in range(n):
        if(c==a or c==b):
            print(s[c],end=" ")
        else:
            print(end=" ")    
    print(" ")        
