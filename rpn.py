#!/usr/bin/env python3

def calculate(arg):
    stack = list()
    for token in arg.split():
        try:
            value = int(token)
            stack.append(value)
        except ValueError:
            arg1 = stack.pop()
            arg2 = stack.pop()
            return arg1 + arg2

    #print(stack)
#pass is a no operation 

def main():
    while True:
            print(calculate(input('rpn calc> ')))

#this code is module runner. It makes the module executable
# __ -> dunder name is a specail variable
#single and double quotes is the same
#this just executes things as we go along.
#name of a module is usually the file name.
#if this program runs by itself, then its module name will be main
#else it will assume it to be the name of the file, ie: rpn
if __name__ == '__main__':
        main()
