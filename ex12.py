# I jumped ahead when doing exercise 11!

age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you're %r old, %r tall and %r heavy" % (
    age, height, weight)

# Remember: %r is for raw representation - debugging; %s is for plain output.

# In PowerShell, to get documentation about the input function:
# > py -m pydoc raw_input