# this is my own data type
class Cookie:
    # constructor
    def __init__(self, color):
        self.color = color

    # new method
    def get_color(self):
        return self.color

    # new method with color parameter
    def set_color(self, color):
        self.color = color

cookie_one = Cookie("green")
cookie_two = Cookie("blue")

print('Cookie one is', cookie_one.get_color())
print('Cookie two is', cookie_two.get_color())
# Cookie one is green
# Cookie two is blue
cookie_one.set_color("yellow")
print('\nCookie one is', cookie_one.get_color())
print('Cookie two is -still-', cookie_two.get_color())
# Cookie one is yellow
# Cookie two is -still- blue

