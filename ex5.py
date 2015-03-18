name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
height_cm = height * 2.54 # centimetres
weight = 180 # pounds
weight_kg = weight * 2.25 # kilogrammes
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %f centimetres tall." % height_cm
print "He's %d pounds heavy." % weight
print "He's %f kilogrammes heavy." % weight_kg
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)