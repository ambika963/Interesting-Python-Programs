##to take student exam score and print their corresponding letter.90-100,80-89 b,70-79 c,0-59 fail
while True:
   a=int(input('Enter your marks out of 100 to check your grade'))
   
   if(a>100 or a<0):
     print('Your grade cannot be defined')
   elif(a<59):
       print('Failed')
   elif(a<70):
       print('Your grade is D')
   elif(a<80):
       print('Your grade is C')
   elif(a<90):
       print('Your grade is B')
   elif(a<=100):
       print('Your grade is A')
   else:
       print('You Grade cannot be defined')