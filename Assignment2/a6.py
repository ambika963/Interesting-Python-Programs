##even number between intervals using function.

def even(l,u):
       print('Even numbers are')
       for i in range(l,u+1):
           if(i%2==0):
               print(f'{ i }')
while True:
   a=input("Do you want to include the boundary elements also(y/n)")
   b=int(input("Enter the lower bound"))
   c=int(input("Enter the upper bound"))
   if(a=='y'):
       even(b,c)
   else:
       even(b+1,c-1)
