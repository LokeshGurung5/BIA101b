def greet():
    #do some complex calculation
    #complex stuff
    print('hello world')

def add_numbers(num1, num2):
    sum = num1 + num2
    print('adding number')
    print(sum)
user1 = 10
user2 = 20
add_numbers(user1, user2)

#other way
def greet():
    # do some calculation code 
    # complex stuffs
    print('Hello')

def add_numbers(num1, num2):
    sum = num1 + num2
    print('adding numbers')
    return sum

userNumber = 10
userNumber2 = 20

returnedSum = add_numbers(userNumber, userNumber2)
print(returnedSum)

