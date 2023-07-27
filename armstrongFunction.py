def armstrong(num,copy,count):
    add=0
    while(num!=0):
        rem=num%10
        add+=rem**count
        num//=10
    if(add==copy):
        return True
    else:
        return False

num=int(input('Enter a Number : '))
print('Armstrong Number' if armstrong(num,num,len(str(num)))else 'Not armstrong Number')
