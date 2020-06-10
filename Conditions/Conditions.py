# looking at if conditions in python
# examples of what works and what doesn't



# Variable Declaration
d = 1
x = 2
c = None
# Conditions

#if(d && d): # Invalid
#    print("yes")

if (d and d): # Valid
    print("yes")
if (d and x):
    print("this will print") # And checks if both exist, not if both are the same
if (d == x):
    print("This will not print")
if (c and x):
    print("this will not print either") # becuase c is None, which is similar to null in most languages
if (c or x):
    print("this will print, because x is satisfied")

# if, elif, and else

if(x == d):
    print(x, " and ", d)
elif(c and x):
    print("this will not print")
else:
    print("Both others failed, so this will print")