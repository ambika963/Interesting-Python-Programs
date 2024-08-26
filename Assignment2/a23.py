#to find quotient and remainder of 2 number
def display(a,b):
    q=int(a/b)
    r=a%b
    print(f"The quotient is { q } and reminder is { r }")
while True:
    dividend=float(input('Enter the dividend  '))
    divisor=float(input('Enter the divisor  '))
    display(dividend,divisor)
    