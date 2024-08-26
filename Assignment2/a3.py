##To find greatest number among three numbers
numbers=[]
positions=['first','second','third','fourth']
for i in range(3):
    a=int(input(f"Enter { positions[i] } number"))
    numbers.append(a)
if(numbers[0]>numbers[1] and numbers[0]>numbers[2]):
    print('First number is greatest.(i.e.{numbers[2]})')
elif(numbers[1]>numbers[0] and numbers[1]>numbers[2]):
    print('second number is greatest.(i.e.{numbers[2]})')
else:
    print(f'Third number is greatest.(i.e.{numbers[2]})')

    