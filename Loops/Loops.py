# Example of loops in python

names = ["sam", "jack", "john"]

while len(names) < 10:
    names.append("another name") # this runs while the condition is not met

print(names)

names = ["sam", "jack", "john"] # reset back to default

for name in names: # simple for each name in names
    print(name)

for idx, name in enumerate(names): # enumerate does a similar thing, but allows you to keep track of an index
    print(idx, name)
    #this is useful for printing the last name in the array
    if(idx == len(names) - 1): # Collections (aka arrays, dictionaries, lists) are numbered from 0..n amount of elements. Len gives us the amount of elements which is 3.
        print(name)

# Using pythons list comprehension to do the same thing
[print(name) for name in names]

# Adding some additional functionality to list comprehension
[print(name) for name in names if name == names[len(names)-1]] # Though this does the same thing as above, it is harder to read, unless you use python regulary

# people do crazy stuff like this sometimes, try not to do this
ages = [1,2,3]
[print(name, "is", ages[nameIdx]) for nameIdx, name in enumerate(names) if nameIdx in [ageIdx for ageIdx, age in enumerate(ages)]]
# It works, but reads and looks terrible.

# How it works
#[ageIdx for ageIdx, age in enumerate(ages)] => [0,1,2]
#[name for nameIdx, name in enumerate(names)] => ["sam", "jack", "john"]
#if nameIdx is in [0,1,2] then use that index in the original ages index to link them

#Looks much better and readable like this
for nameIdx, name in enumerate(names):
    for ageIdx, age in enumerate(ages):
        if nameIdx == ageIdx:
            print(name, "is", age)

# You can mix and match
for nameIdx, name in enumerate(names):
    [print(name, "is", age) for ageIdx, age in enumerate(ages) if nameIdx == ageIdx]

# If you are writing code with others like in DevOps, then it is good practice to decide what style will be used.
# Where I used to work, we would not use list comprehension if there was any condition checks. If we had to check a value
# then we would write out the for loop.