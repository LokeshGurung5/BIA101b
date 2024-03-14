#creation of array
array1 = [1, 2, 3, "thimphu", 2.5]
print(array1)

#retrieving the data
element1 = array1[0]
element2 = array1[4]
print(element1) 

last_element = array1[-5]
print (last_element)

#modifying elements
array1[0] = 10
print(array1)

#getting numbers of element in an array
no_of_elements = len(array1)
print(no_of_elements)

#slicing element
elements = array1[0:2]
print(elements) 

#adding to stack
stackvar = []
stackvar.append(4)
stackvar.append(2)
stackvar.append(9)
stackvar.append(1)
print('after appending', stackvar)
stackvar.pop()
print('after popping', stackvar)

#apend
arr1 = [1, 2, 3]
arr1.append(4)
print(arr1)

#insert in specific location
