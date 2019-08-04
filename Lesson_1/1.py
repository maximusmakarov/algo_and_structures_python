# 1.	Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

number = int(input('Введите 3-х значное число: '))
number1 = number
amount = 0
multi = 1

while number > 0:
    digit = number % 10
    amount += digit
    multi *= digit
    number //= 10
print(f'Сумма цифр числа {number1} равна  {amount} \nПроизведение цифр числа {number1} равна {multi}')
