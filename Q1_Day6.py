#add = a + b
#multiply = a * b
#divide = a / b
#subtract = a - b
operator = input()
operator = str(operator)
a = input()
a = int(a)
b = input()
b = int(b)
if operator == 'add':
        print("addition = ",a+b)
elif operator == 'subtract':
        print("Subtraction =",a-b)
elif operator == 'multiply':
        print("Multiplication = ",a*b)
elif operator == 'divide':
        print("Division = ",a/b)

