print('lol')
name='vova'
age='29'

def print_numbers(x):
    if x <= 5:  # Базовый случай: если x больше 0
        print(x)  # Выводим текущее значение x
        print_numbers(x + 1)  # Рекурсивный вызов с уменьшенным значением x

x = 1 # Пример числа для рекурсии
print_numbers(x)

print(f"my name is {name}, and my age is {age}")

my_string = input('enter a number')

if my_string.isdigit():
    my_integer=int(my_string)
    print(my_integer)
else:
    print(f"{my_string} is not a number")
    
print(my_string.format(price=49))