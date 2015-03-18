formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4) # We get: 1 2 3 4
print formatter % ("one", "two", "three", "four") # We get: 'one' 'two' 'three' 'four'
print formatter % (True, False, False, True) # We get: True False False True
print formatter % (formatter, formatter, formatter, formatter) # We get: '%r %r %r %r' '%r %r %r %r' (and twice more)
print formatter % (
    "I had this thing.",
    "That you could type right,",
    "But it didn't sing.", # Apostrophe fiddles with the '/"-ness!
    "So I said goodnight."
) # We get: 'I had... ' 'That... ' "But it didn't sing." 'So... ' (all on one line)
