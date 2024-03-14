#loops over an array
fruits = ['a', 'b', 'c']

#for (anyVarName) in varName
for fruit in fruits:
    print(fruit)

#loop through each element
#at each stage, if the element is 'c'
#print true
for e in fruits:
    if e == 'c':
        print('TrueFromC')
    if e == 'b':
        print('TrueFromB')

#iterte over a string
greeting = 'hello'
for char in greeting:
    #check if the string contains vowel
    if char == 'a':
        print('It contains vowel')
    elif char == 'e':
        print('It contains vowel')
    elif char == 'i':
        print('It contains vowel')
    elif char == 'o':
        print('It contains vowel')
    elif char == 'u':
        print('It contains vowel')

#iterate over a range
for i in range(5, 14, 2): #range(start, stop, step) 
    print(i) #ouptut 5,6,7,8,9,10,11,12,13

#another way
for i in range(8):
    val = i + 5
    print(val) #output 5,6,7,8,9,10,11,12,13


#while loops

#basic while loop
count = 0
while count < 5:
    print(count)
    count = count + 1

#user input string is unknown
#print every char of the string
s = 'berbfowqb'
counter = 0 
lenth_s = len(s)
print('Counter', counter)
print('len s', lenth_s)
print("going through loop")

while counter < lenth_s:
    print('counter', counter)
    char = s[counter]
    print(char)
    counter = counter + 1
    print('-------')
    