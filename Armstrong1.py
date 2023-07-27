num=int(input('Enter a Number : '))
copy=num
count=len(str(num))
add=0
while(num!=0):
    rem=num%10
    add+=rem**count
    num//=10
if(copy==add):
    print('Armstrong number')
else:
    print('Not armstrong number')
