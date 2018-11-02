#!/usr/bin/env python3
#import operator
#
#op = {
#        '+': operator.add,
#        '-': operator.sub,
#        '*': operator.mul,
#        '/': operator.truediv,
#        }
#
#def calculate(arg):
#    stack = arg.split()
#    while len(stack) > 1:
#            token = stack.pop()
#            try:
#                value = int(token)
#                stack.append(value)
#            except ValueError:
#                val2 = int(stack.pop())
#                val1 = int(stack.pop())
#                stack.append(op[token](val1, val2))
#                continue;
#
#    return int(stack[0])
#    '''for token in arg.split():
#        if token == '+' | token == '-' | token == '*' | token == '/':
#            num1 = stack.pop()
#            num2 = stack.pop()
#            result = op[token](arg2, arg1)
#            stack.append(result)
#            continue
#
#       try:
#           value = int(token)
#           stack.append(value)
#       except ValueError:
#           print 'BAD RPN eq'
#           return -1000000000000000000
#
#    return stack[0]
#
#    '''
##try:
#             #   value = int(token)
#              #  stack.append(value)
#
#           # except ValueError:
#            #    arg1 = stack.pop()
#             #   arg2 = stack.pop()
#            #  result = op[token](arg2, arg1)
#
#             #   stack.append(result)
#           # return stack[0]
#
#
#
##pass is a no operation 
#def main():
#    while True:
#        print(calculate(input('rpn calc> ')))
#
##this code is module runner. It makes the module executable
## __ -> dunder name is a specail variable
##single and double quotes is the same
##this just executes things as we go along.
##name of a module is usually the file name.
##if this program runs by itself, then its module name will be main
##else it will assume it to be the name of the file, ie: rpn
#if __name__ == '__main__':
#    main()
#!/usr/bin/env python3

import operator


operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}

def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
        print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    while True:
        result = calculate(input("rpn calc> "))
        print("Result: ", result)

if __name__ == '__main__':
    main()

