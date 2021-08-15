sum=0
num=int(input())
temp=num
while(num):
    ini=1
    fact=1
    rem=num%10
    while(ini<=rem):
        fact=fact*ini
        ini=ini+1
    sum = sum+fact
    num = num//10
if(sum == temp):
    print("Yes it is a strong number")
else:
    print("Not a strong number")
