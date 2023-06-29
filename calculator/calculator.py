def add (a, b) :
    return (a + b)

def subtract (a, b) :
    return (a - b)

def multiply (a, b) :
    return (a * b)

def divide (a, b) :
    return (a / b)

print ('''Select operation to perform : \n
        1. Addiion \n
        2. Subtraction \n
        3. Multiplication \n
        4. Division \n''')

x = float(input('Enter the first number '))
y = float(input('Enter the second number '))

while True :
    select = int(input('Select operation from 1, 2, 3, 4 : '))

    if select == 1 :
        print(x, '+', y, '=', add(x, y))

    elif select == 2 :
        print(x, '-', y, '=', subtract(x, y))

    elif select == 3 :
        print(x, '*', y, '=', multiply(x, y))

    elif select == 4 :
        print(x, '/', y, '=', divide(x, y))
    
    else :
        break

print('Operations cannot be performed !')