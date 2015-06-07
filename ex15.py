from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

txt.close()

# print "Type the filename again:"
# file_again = raw_input("> ")

# txt_again = open(file_again)

# print txt_again.read()

# txt_again.close()

# In PowerShell type 'py' to enter interactive mode.
# Try: txt = open('ex15_sample.txt') - not forgetting the quotation marks!
# Try: txt.read() to see the file's contents.
# Try: txt.read() to see... nothing.
# Try: txt.close() then open and read to see the contents again.
# Try: txt.close() then read to see an error about i/o on a closed file.
