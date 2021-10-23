''' You are given a string .
Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, 
lowercase and uppercase characters.

##output format
Output Format

In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
In the second line, print True if  has any alphabetical characters. Otherwise, print False.
In the third line, print True if  has any digits. Otherwise, print False.
In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
In the fifth line, print True if  has any uppercase characters. Otherwise, print False.
'''

if __name__ == '__main__':
    s = input('Give input  - ')
    print(s.isalnum())
    x =False
    y = False
    z =False
    w =False
    for i in s:
        if (i.isalpha()):
            x = True
    
        if(i.isdigit()):
            y = True
         
        if(i.islower()):
            z = True
            
        if(i.isupper()):
            w = True
           
    print('%s\n%s\n%s\n%s'%(x,y,z,w))