def nearestStrong(n,i):
    pre = n-i 
    next = n+i
    
    for num in [pre,next]:
        sum = 0
        temp = num
        while(temp):
            ini = 1
            fact = 1
            rem = temp % 10
            while(ini <= rem):
                fact = fact*ini
                ini = ini+1
            sum = sum+fact
            temp = temp//10
        if(sum == num):
            return num
        else:
            return nearestStrong(n,i+1)

    

nums = [int(i) for i in input().split(',')]
dict_nums = {}
for num in nums:
    temp = num
    sum = 0
    while(temp):
        ini = 1
        fact = 1
        rem = temp % 10
        while(ini <= rem):
            fact = fact*ini
            ini = ini+1
        sum = sum+fact
        temp = temp//10
    if(sum == num):
        dict_nums.update({num:"strong"})
    else:
        alt = nearestStrong(num,1)
        dict_nums.update({num:["Not Strong",alt]})

print(dict_nums)



