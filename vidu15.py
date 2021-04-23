#sys.argv

import sys

script, filename = sys.argv
txt = open(filename)
print("Here's your file %r" %filename)
print(txt.read())
print('Type the filename again:')
filename_again = input(">")
txt_again = open(filename_again)
print(txt_again.read())