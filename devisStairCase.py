#recursive way to climb satirs
def stepPerms(n):
    arr = [0]*(n+2)
    arr[0] =1
    arr[1] =1
    arr[2] = 2
    for i in range(3,n+1):
        arr[i] = arr[i-3]+arr[i-2]+arr[i-1]
    return arr[n]
    # if (n ==1 or n ==0):
    #     return 1
    # elif(n == 2):
    #     return 2
    # else:
    #     return stepPerms(n-3)+stepPerms(n-2)+stepPerms(n-1)
    # # Write your code here