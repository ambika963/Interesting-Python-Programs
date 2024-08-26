#suppose you  often go to a restaurant with firends and you have to split amount of bill write a program to calculate the split amount of bill.
def split(a,b):
    return a/b
a=float(input('Enter total bill amount   '))
b=float(input('Total friends?    '  ))
a=split(a,b)
print(f'The amount that each have to pay is { a }')