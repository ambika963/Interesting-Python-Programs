while True:
    a = int(input('Enter a year to test whether it is a leap year or not: '))
    if a % 4 == 0:
        if a % 100 == 0:
            if a % 400 == 0:
                print('It is a leap year')
            else:
                print('It is not a leap year')
        else:
            print('It is a leap year')
    else:
        print('It is not a leap year')

    # Ask the user if they want to continue
    choice = input("Do you want to check another year? (yes/no): ").lower()
    if choice != 'yes':
        print("Exiting the program.")
        break
