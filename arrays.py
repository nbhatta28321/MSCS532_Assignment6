
def insert(arr, nums):

    temp_arr = [0] * (len(arr) + 1) #increase size by 1

    for i in range(len(arr)): #copying array 
        temp_arr[i] = arr[i]

    temp_arr[len(arr)] = nums   #adding to the end 

    return temp_arr

def delete(arr, index):

    if index < 0 or index > len(arr):
        return "Out of Index"

    temp_arr = [0] * (len(arr) - 1) #decrease size by 1

    for i in range(index): #copy until the index
        temp_arr[i] = arr[i]

    for i in range(index+1, len(arr)):     #shift all the numbers starting from index
        temp_arr[i-1] = arr[i]

    return temp_arr


def access(arr, index):

    if index < 0 or index > len(arr):
        return "Out of Index"
    
    print(f"The value at index {index} is {arr[index]}")
    return
    
arr = [1,2,3]
arr = insert(arr, 4)
print(arr)
arr = insert(arr, 6)
arr = insert(arr, 8)
print("After Insertion",arr)

arr = delete(arr, 3) # has to delete 4
print(arr)

access(arr, 1)







