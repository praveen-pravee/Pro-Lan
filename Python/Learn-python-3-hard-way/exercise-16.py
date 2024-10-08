# title: Reading and Writing Files
# Now we are working with files

"""
STUDY DRILLS:
-------------
In this exercise we are working on a file in writing, the opening command was just open(),
the task was writing so we used 'w' in the file, open(file, 'w'),
And we want to erase the file, so the method is truncate(),
input into the writing on the file what is the writing command or method,
Just write(), and you comment out, and it's easy to understand.
"""
from sys import argv 

script, filename = argv

print(f"We Are going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening File...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line_1 = input("line 1")
line_2 = input("line 2")
line_3 = input("line 3")

print("I'm going to write these to the file.")

target.write(line_1)
target.write("\n")
target.write(line_2)
target.write("\n")
target.write(line_3)
target.write("\n")

print("And finally, we close it.")
target.close()


