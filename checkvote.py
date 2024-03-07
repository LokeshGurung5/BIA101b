# ! check if user can vote

# ?Get user age from input
# ?convert userinput(str) to int() to number
# ?check if user can vote
# ?if else statement
# ?if above 18, print "You can vote"
# ?if below 18, print "You canot vote"
userInput = input("enter your age: ")

userAge = int(userInput)

if userAge > 18:
    print("you can vote")
else:
    print("you cannot vote")