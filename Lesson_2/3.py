"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
"""
# Без рекурсии

num = int(input('Введите число: '))
revNum = 0

while num > 0:
    revNum = revNum * 10 + num % 10
    num //= 10

print(revNum)


# С рекурсией

def reverse(num, revnum=0):
    if num == 0:
        return revnum
    else:
        return reverse(num // 10, revnum * 10 + num % 10)


num = int(input('Введите число: '))
print(reverse(num))
