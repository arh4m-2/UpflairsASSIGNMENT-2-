def palindrome(str1):
    reversed_str = str1[-1::-1]
    if reversed_str.lower() == str1.lower():
        return True
    else:
        return False

print(palindrome("Nitin")) 


def counter(str1):
    count_list = []
    for char in str1:
        count = 0
        ch = char
        for ch in str1:
            if ch == char:
                count +=1
        count_list.append(count)
    for i in range(len(str1)):
        print(f'{str1[i]} : {count_list[i]}')


counter('arham')


def calculator(num1, num2, operation):
    
    if operation == 'Add':
        print(f'Addition of {num1} and {num2} : {num1+num2}')
    if operation == 'Subtraction':
        print(f'Difference of {num1} and {num2} : {num1-num2}')
    if operation == 'Multiplication':
        print(f'Multiplication of {num1} and {num2} : {num1*num2}')
    if operation == 'Division1':
        print(f'Division of {num1} and {num2} : {num1/num2}')

x = int(input("Enter first number : "))
y = int(input("Enter second number : "))
z = input("Enter Operation : ")
calculator(x,y,z)


def rightAnglePattern(n):
    for i in range(n):
        for j in range(i + 1):
            print('*', end="")
        print('')        
       
x = int(input('Enter No. Of Rows : ' ))
rightAnglePattern(x)


def multiplication_table(n):
    for i in range(1,11):
        print(f'{n} x {i} = {n*i}')

x = int(input('Enter a number : '))
multiplication_table(x)
