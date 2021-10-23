'''
You are given a string s consisting of lowercase English letters and/or '_' (underscore).
You have to replace all underscores (if any) with vowels present in the string.

The rule you follow is:
Each underscore can be replaced with any one of the vowel(s) that came before it.

You have to tell the total number of distinct strings we can generate following the above rule.
'''

def canYouCount (s):
    #i = 1
    num = 1
    count = 0
    vowels = ['a','e','i','o','u']
    for i in s:
        if (i == '_' and count >=1):
            num *=count
        elif (i in vowels):
            vowels.remove(i)
            count+=1
    return num
    

T = int(input('Number of input'))
for _ in range(T):
    s = input('Give Your input')

    out_ = canYouCount(s)
    print (out_)
    # write your code here