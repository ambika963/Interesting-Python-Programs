#generate the multiplication table of 5.
while True:
  a=int(input('You want multiplication table of which number?  '))
  for i in range(1,11):
      print(f'{ a } * { i } = { i*a }')