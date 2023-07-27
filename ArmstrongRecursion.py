def armstrong(num,count):
    if(num==0):
        return 0
    return (num%10)**count+armstrong(num//10,count)
num=int(input('Enter a Number : '))
print('Armstrong Number' if armstrong(num,len(str(num))==num)else 'Not armstrong Number')
