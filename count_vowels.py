#counting vowels in given string
string = input('enter the string :: ')

count = 0
for i in string:
    if i == 'a' or i == 'o' or i == 'e' or i == 'i' or i == 'u':
        count +=1
print('Numbers of vowels in the string are :: ', count)