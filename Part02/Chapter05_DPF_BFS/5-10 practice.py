array = [[0, 0],
         [2, 20],
         [3, 30]]
if array[0][0] == False:
    array[0][0] = True
print(array[0][0], bool(array[0][0]))
array[0][0] = 1
print(array[0][0])
print(bool(array[0][0]))