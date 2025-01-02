operator_stack = []
value_stack = []

question = "(1+((2+3)*(4*5)))"

for token in question:
    # if token is a number
    if(token.isnumeric()):
        value_stack.append(token)
    elif(token == '('):
        # do nothing
        pass
    elif(token == ')'):
        # pop the two elements from value stack
        # pop one element from operator stack
        # perform the computation
        # add result to value stack
        second_num = value_stack.pop()
        first_num = value_stack.pop()
        operation = operator_stack.pop()
        result = eval(str(first_num)+str(operation)+str(second_num))
        value_stack.append(result)
    else:
        # this is a mathematical operation
        operator_stack.append(token)

print("Result is ")
print (value_stack[0])