while True:
  import random
  n=["","Scisor","Paper","Rock"]
  a=int(input(f'Enter\n1 for scisor\n2 for Paper\n3 for Rock'))
  print(f'You choosed { n[a] }')
  q=int(random.randrange(1,4))
  print(f"Computer choosed { n[q] }")
  if(q==a):
      print('Game tied.Try again!')
      continue
  elif(a==1 and q==2):
      print('You wined')
  elif(a==2 and q==3):
      print('You wined')
  elif(a==3 and q==1):
      print('You wined')
  else:
      print('Computer wined')
  x=input("Do you want to play again?(y/n)").lower()
  if(x!='y'):
      print('Thanks for playing')
      break