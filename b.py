#my answer
input_str = '((()))' 
stack = []
for char in input_str:
    if char == '(':
        stack.append(char)
    if char == ')':
        stack.pop()

if len(stack) == 0:
    print('True')
else:
    print('False')




