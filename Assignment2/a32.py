try:
    a=int(input('Enter the number'))
    c=10/a
    print(f'The quotient is { c }')
except ZeroDivisionError:
    print('You cannot divide any number by 0')
finally:
    print('Finally divide gariyo kta ho')