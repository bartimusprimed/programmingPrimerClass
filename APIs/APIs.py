# An example of using APIs and how they align with library calls

# Tell python the library you intend to use
import os

# Using this library you can call the popen API, this will print out the system information
pipe = os.popen("systeminfo")
for line in pipe.readlines():
    print(line)
pipe.close()


# This is an api that utilizes another api, which is sometimes called a wrapper, as it parses some of the information you send.

# using help(os.popen) can will give you the definition of the API:

# Help on function popen in module os:

# popen(cmd, mode='r', buffering=-1)
#     # Supply os.popen()

# This tells you that the first arguement to popen is the cmd, anything that has a name and an = sign like mode='r', means that a default is provided.
# Using help() in python is extremely useful

from requests import request

help(request)

# This is also extremely useful when you do not have an internet connection to look at the docs.