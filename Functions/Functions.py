# example of using functions in python


name = "Sam"
name2 = "Steve"
name3 = "Jack"

print(name) # print is a function
print(name2)
print(name3)

# Making your own function

def say_hi(name):
    print("Why hello there,", name)


# Allows you to wrap the print function
say_hi(name2)

# Functions just allow you to save time, anything you do in a function you should be able to do in code.
def greeter(name1, name2):
    print(name1, "says hello to", name2)

# Notice how we reused name1 and name2 as arguments. This is actually what makes a function different than writing inline code
# The namespace changes, in technical nerd language this is considered a "stackframe"
# There is a logical separation between the names, this logical separation is the stack's base pointer.
greeter(name2,name)
greeter(name3, name)
greeter(name2,name3)

# Lambdas
say_bye = lambda name: print("byeeeeee, ", name)

say_bye(name2)
say_bye(name3)
say_bye(name)

# Python does have a version of closures which share a namespace

def say_hello(name):
    print("ughhhhh", name2) # This is allowed
    print("Hi", name)
    def say_bye():
        name4 = "jimmy"
        print("Bye", name)
    say_bye()
    # print(name4) # This isn't allowed though

say_hello(name)
say_hello(name2)
say_bye(name) # notice how this is the same name as the one in say_hello, this works because our other stackframe collapsed and we are now back in the normal one
