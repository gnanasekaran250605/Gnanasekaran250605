a=[]
num=int(input("Enter a n natural number:"))
for i in range(1,num+1):
    a.append(i)
print(a)

sum=0
for i in a:
    sum=sum+i
print(sum)
