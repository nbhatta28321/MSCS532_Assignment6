
def insert(matrix, row, column, value):

    if row < 0 or row > len(matrix) or column < 0 or column > len(matrix):
        print("Out of index")
        return
    
    matrix[row][column] = value

    print('After insersion')

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j])

    return 

def delete(matrix, row, column):

    if row < 0 or row > len(matrix) or column < 0 or column > len(matrix):
        print("Out of index")
        return
    
    matrix[row][column] = '-'

    print('After deletion')

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j])
    
    return


def access(matrix, row, column):

    if row < 0 or row > len(matrix) or column < 0 or column > len(matrix):
        print("Out of index")
        return
    
    print(f" the serached item is {matrix[row][column]}")

    return
    
matrix = [ [1,2,3], [3,4,5], [6,7,8]]
insert(matrix, 1 , 2, 77)
delete(matrix, 1 , 2)
access(matrix, 1 , 0)







