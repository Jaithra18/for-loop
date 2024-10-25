x=int(input("Enter some numbers you want to find the sum of"))
sum=0
for i in range(1,x+1):
    sum=sum+i
    print(sum)
    
y=int(input("Enter a number"))
for i in range(y,0,-1):
    print(i)
    
z=input("Enter your own string")
s=("")
for i in z:
    s=i+s
print(s)    