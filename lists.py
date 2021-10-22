'''Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command 
will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.'''

if __name__ == '__main__':
    N = int(input('Enter Number of commands - '))
    #print(N)
    i = 0
    arr = []
    while(i < N):
        command,*inputVal = input('Enter Your Command- ').split()
        
        if command == 'insert':
            arr = arr[:int(inputVal[0])] +[int(inputVal[1])] +arr[int(inputVal[0]):]
        elif command == 'print':
            print(arr)
        elif command == 'remove':
            arr.remove(int(inputVal[0]))
        elif command == 'append':
            arr.append(int(inputVal[0]))
        elif command  == 'sort':
            arr.sort()
        elif command == "reverse":
            arr.reverse()
        elif command == 'pop':
            arr.pop()
        i+=1
    #print(command,inputVal,arr)