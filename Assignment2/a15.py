##To calculate sum of natural numbers3
while True:
  a = int(input('Enter the natural number till which we want sum: '))
  y = 0  # Initialize y to 0
  
  for i in range(a + 1):
      y = y + i  # Accumulate the sum
  
  print(f'The sum is { y }')
