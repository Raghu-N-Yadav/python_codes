#defult order
string1 = '{} {} {}'.format('raghu','N','yadav')
print(string1)
#ordered formatting
string1 ='{1} {0} {2}'.format('raghu','yadav','N')
print(string1)
#keyword formatting 
string1 =' {a} {b} {c}'.format(b = 'N',a = 'Raghu', c = 'yadav')
print (string1)