char = input()
password = ''

char = char.replace('i', '!')
char = char.replace('a', '@')
char = char.replace('m', 'M')
char = char.replace('B', '8')
char = char.replace('o', '.')

char = char + 'q*s'

print(char)