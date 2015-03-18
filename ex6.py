x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not) # Two string-in-strings

print x
print y

print "I said: %r." % x # Third
print "I also said: '%s'." % y # Fourth

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious # Isn't that five?

w = "This is the left side of..."
e = " a string with a right side."

print w + e