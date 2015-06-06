from sys import argv

args = len(argv)
print "Number of arguments:", args

if args == 3:
    script, first, second = argv
    print "You forgot the third argument!"
    third = raw_input("Third argument please: ")
else:
    script, first, second, third = argv # Will fail is args < 3

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
