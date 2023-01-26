'''
def func_one():
    func_two()
    print('One')
'''


# once func_one calls func_two, func_two gets pushed on the call stack
'''
def func_two():
    func_three()
    print('Two')

def func_one():
    func_two()
    print('One')
'''


# once func_two calls func_three, func_three gets pushed on the call stack
# func_three does not call any other function. 
# once it is done running, we pop func_three from that call stack. 
'''
def func_three():
    print('Three') # once it prints out the string, it is done running

def func_two():
    func_three()
    print('Two')

def func_one():
    func_two()
    print('One')

# Three
'''


# now I have func_two as at the top of the call stack
# it was wating for func_three to finish running.
# once it is done running, we pop func_two from that call stack. 
'''
def func_two():
    # func_three() -> after it prints 'Three'
    print('Two') # func_two can print out the string and it is done running

def func_one():
    func_two()
    print('One')

# Three
# Two
'''


# now I have func_one as at the top of the call stack
# it was wating for func_two to finish running.
# once it is done running, func_one can be popped from that call stack. 
'''
def func_one():
    func_two() # -> after it prints 'Two'
    print('One') # func_one can print out the string and it is done running

# Three
# Two
# One
'''

# I called these functions in the order of
# func_one
# func_two
# func_three

# but, it printed out (this is the order that came off of the call stack)
# Three
# Two
# One

