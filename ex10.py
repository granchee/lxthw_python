import time

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

fat_cat_2 = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print fat_cat_2

# Escape Sequences
bel_string = "Can you hear the bells?"
bs_string = "Boot or boo\bt?"
cr_string = 'This string is going to be\rOVERWRITTEN!'
a_string = "Is this an 'A'? \x41"

print bel_string,
print "\a",
time.sleep(0.5) # 500 ms
print "\a"
print bs_string
print cr_string
print a_string

# while True:
    # for i in ["/", "-", "|", "\\", "|"]:
        # print "%s\r" % i,
        # time.sleep(0.1)
        
# Study Drills
backslashes_str = "\\"
print "%s One backslash?" % backslashes_str
print "%r Two backslashes? With delimiters?" % backslashes_str
