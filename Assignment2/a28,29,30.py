#postional argument
def sum(a,b):
    print(f'Sum is { a+b }')
sum(2,3)
#keyword argument
def difference(a,b):
    print(f'Difference is { a-b }')
difference(b=2,a=6)
#default argument
def intro(name,age='Between 0 to 100'):
    print(f'The name is { name } and age is { age }')
intro('Sandesh')
intro('Sarthak',30)
#Passing tuples
def display(*args):
    for i in args:
        print(i)
a=(1,2,5,2,4)
display(*a)
#passing Dictionaries
def display(**kwargs):
    for key,value in kwargs.items():
        print(f'Key:{ key }  Value:{ value}')
r={
    "name":'Sandesh',
    'address':'Pokhara'
}
display(**r)