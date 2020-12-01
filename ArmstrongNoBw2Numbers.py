#Armstrong number between two numbers
print("Enter the start and the end number")
start,end=map(int,input().split())
for i in range(start,end+1):
    summ=0
    ip=i
    while ip>0:
        temp=ip%10
        summ=summ+temp**3
        ip=ip//10
    if(i==summ):
        print(summ)
    