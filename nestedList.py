'''Given the names and grades for each student in a class of  students,
 store them in a nested list and print the name(s) of any student(s) having the second lowest grade.'''

if __name__ == '__main__':
    arr = []
    arr2  = []
    arr3 = []

    for _ in range(int(input('Number of students ?? -'))):
        name = input('Enter name ')
        score = float(input('enter score '))
        arr = [name,score]
        arr2.append(arr)
        arr3.append(score)
    arr3.sort()
    x  = arr3[1]
    y  = []
    for val in arr2:
        if val[1] == x:
          y.append(val[0])  
    y.sort()
    for i in y:
        print(i)
    #print (arr2,x,y)
    