char = input()
min = 0
max = len(char)-1
result = True
while(min<max):
    if(char[min]==' '):
        min+=1
    elif(char[max]==' '):
        max-=1
    elif(char[min]!=char[max]):
        result = False
        break
    else:
        min+=1
        max-=1
if (result):
    print(char, 'is a palindrome')
else:
    print(char, 'is not a palindrome')
