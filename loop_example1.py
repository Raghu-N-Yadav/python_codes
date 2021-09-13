#code to check break, continue and pass statement
s = 'Raghunandan Yadav'
for letter in s:
    if letter == 'n':
        break
    print(letter, end = ' ')
print('\n')

for letter in s:
    if letter == 'n':
        continue
    print(letter, end = ' ')
print('\n')
for letter in s:
    if letter == 'n':
        pass
    print(letter, end = ' ')
print('\n')