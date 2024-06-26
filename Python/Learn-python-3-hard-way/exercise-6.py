# title: Strings and Text
# single quotes or double quotes and format the string.
"""
STUDY DRILLS:
-------------
Python also has another kind of formatting using the .format() syntax,
which you see on line 27 & 29. You’ll see me use that sometimes when 
I want to apply a format to an already-created string, 
such as in a loop. We’ll cover that more later.
"""

type_of_people = 10
x = f"There are {type_of_people} types of people."

binary = 'binary'
do_not = "don't"

y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = True
joke_evalution = "Isn't that joke so funny?! {}" # note this {} character

print(joke_evalution.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
