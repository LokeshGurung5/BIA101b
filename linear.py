#searching
#sorting

#problem_1
#input
user_input = [1, 2, 3, 4, 5, 6, 7, 8]

#check to see if a certain number exist in the user input array
n = 2
#linear search
for i in user_input:
    if i == n:
        print('The number', n, 'does exist')    

#another way of linear search
result = False
for i in user_input:
    if i == n:
        result = True

if result == True:
    print('found')
else:
    print('not found')

#break and continue concept
input = [1,2,3,4,5]
for i in input:
    print('hi')
    if i == 1:
        continue #skip to the next iteration of the for loop
        break #stop the for loop if the statement is true

#space, when using an array and if the value is been input to the array
#the space changes, the space will be O(n)
#interms of variable, the space is constant  
    
