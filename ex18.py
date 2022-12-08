
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

#the * in *args tells Python to take all the arguments to the function and then put
#them in args as a list. It’s like argv that you’ve been using but for functions. It’s not normally
#used too often unless specifically needed.

def print_two_again(arg1,arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")



def print_one(arg1):
    print(f"arg1:{arg1}")


def print_none():
    print("I got nothing'.")


print_two("Zed", "Shaw")
print_two_again ("Zed", "Shaw")
print_one("First!")
print_none()

    
