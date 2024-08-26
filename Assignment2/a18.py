#to create a simple calculator (add,sub,mul,div)
while True:
  c=input('Select the operation by typing operator symbol(+,-,*,/)  ')
  a=int(input('Enter first operand'))
  b=int(input('Enter second operand'))
  if(c=='+'):
      print(f'The sum is { a+b }')
  elif(c=='-'):
      print(f'The difference is { a-b }')
  elif(c=='*'):
      print(f'The difference is { a-b }')
  elif(c=='/'):
      print(f'The quotient is { a/b }')
  else:
      print('Please enter correct data')