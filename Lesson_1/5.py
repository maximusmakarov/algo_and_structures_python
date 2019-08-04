# 5.	Пользователь вводит две буквы. Определить, на каких местах
# алфавита они стоят, и сколько между ними находится букв.

char1 = 0
char2 = 0

while char1 == char2 or char1.isdigit() or char2.isdigit():
    char1 = input('Ведите 1-ю букву: ')
    char2 = input('Ведите 2-ю букву: ')

    if char1 == char2:
        print('Введите разные буквы!')

    if char1.isdigit() or char2.isdigit():
        print('Введите только буквы!')

char1 = ord(char1) - ord('a') + 1
char2 = ord(char2) - ord('a') + 1

print(f'Введённые буквы стоят на позициях {char1} и {char2}\nБукв между ними {abs(char2 - char1) - 1}')
