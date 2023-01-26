def func_three():
    print('Three')

def func_two():
    func_three()
    print('Two')

def func_one():
    func_two()
    print('One')

func_one() 
# Three
# Two
# One


# go to vs code run and debug 
# mark func_one() as breakpoint
# focus on call stack section

