#reading a file

from sys import argv

script, file_name = argv
txt = open(file_name)
print('this is your file \n%s' %file_name)
print(txt.read())

sec = input('name of your second file ??\t')
txt_m = open(sec)
print('this is written is this\n', txt_m.read())