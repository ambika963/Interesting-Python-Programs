def simple(p,t,r):
 return ((p*t*r)/100)
while True: 
 a=int(input('Enter Principle '))
 b=int(input('Enter Time  '))
 c=int(input('Enter Rate  '))
 x=simple(a,b,c)
 print(x)
