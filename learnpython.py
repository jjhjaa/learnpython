# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#
#""" 
#age = raw_input("How old are you? ")
#height = raw_input("How tall are you? ")
#weight = raw_input("How much do you weigh? ")
#
#print "So you're %r old, %r tall and %r heavy." % (
#    age, height, weight)
#"""
#
#
#""" 
#from sys import argv
#
#script, first, second, third = argv
#
#print "The script is called:", script
#print "Your first variable is:", first
#print "Your second variable is :", second
##print "Your third variable is:", third
#""""

#from sys import argv

#script, user_name = argv
#prompt = "> "

#print "Hi %s. I'm the %s script." % (user_name, script)
#print "I'd like to ask you a few questions."
#print "Do you like me %s?" % user_name
#likes = raw_input(prompt)

#print "Where do you live %s?" % user_name
#lives = raw_input(prompt)

#print "What kind of computer do you have?"
#computer = raw_input(prompt)

#print """
#ALright, so you said %r about liking me.
#You live in %r. Not sure where that is.
#And you have a %r computer. Nice.
#""" % (likes, lives, computer)


#from sys import argv

#script, filename = argv

#txt = open(filename)

#print "Here's your file %r:" % filename
#print txt.read()

#print "Type the filename again:"
#file_again = raw_input("> ")
#txt_again = open(file_again)

#print txt_again.read()

#from sys import argv

#script, filename = argv

#print "We're going to erase %r." % filename
#print "If you don't want that, hit CTRL-C (^C)."
#print "If you do want that, hit RETURN."

#raw_input("?")

#print "Opening the file..."
#target = open(filename, 'w')

#print "Truncating the file.  Goodbye!"
#target.truncate()

#print "Now I'm going to ask you for three lines."

#line1 = raw_input("line 1: ")
#line2 = raw_input("line 2: ")
#line3 = raw_input("line 3: ")

#print "I'm going to write these to the file."

#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

#print "And finally, we close it."
#target.close()


from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" (from_file, to_file)

# we could do these on one line, how ?

in_file = open(from_file)
indata = in_file.read()

print "the input file is %d bytes long" % len(indata)

print "does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "alright all done."

out_file.close()
in_file.close()



