#binary search

Array = [ 3, 4, 5, 6, 7, 8, 9]
target = 9

low = 0
high = len(Array) - 1

#loop
result = False
while low <= high:
    #mid
    mid = (low + high) // 2
    
    #compare my value with the target
    if Array[mid] == target:
        result = True
        break

    #compare and discard the half
    if target > Array[mid]:
        low = mid + 1
    else:
        high = mid - 1

if result == True:
    print('found')
else:
    print('not found')