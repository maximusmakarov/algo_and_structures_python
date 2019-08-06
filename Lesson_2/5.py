"""
5.	Вывести на экран коды и символы таблицы ASCII, начиная с символа
под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""

for ascii in range(32, 128):
    print(ascii, '-', chr(ascii), end=' ')
    if ascii < 100:
        print('', end=' ')
    if (ascii - 1) % 10 == 0:
        print()

# С рекурсией


def ascii_codes(first, second, row=10, column=10):
    if first > second:
        return ''

    if row == 0:
        return f'\n{first}-{chr(first)} {ascii_codes(first + 1, second, column - 1)}'

    return f'{first}-{chr(first)} {ascii_codes(first + 1, second, row - 1)}'


print(ascii_codes(32, 127))
