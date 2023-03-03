#Programming languages offer a method of storing data for reuse. If there is a greeting we want to present,
# a date we need to reuse, or a user ID we need to remember we can create a variable which can store a value. In Python,
# we assign variables by using the equals sign (=).

message_string = "Hello there"
# Prints "Hello there"
print(message_string)

#Variables can’t have spaces or symbols in their names other than an underscore (_).
# They can’t begin with numbers but they can have numbers after the first letter (e.g., cool_variable_5 is OK).

# Greeting
message_string = "Hello there"
print(message_string)

# Farewell
message_string = "Hasta la vista"
print(message_string)

#Above, we create the variable message_string, assign a welcome message,
#and print the greeting. After we greet the user, we want to wish them goodbye.
# We then update message_string to a departure message and print that out.

# We've defined the variable "meal" here to the name of the food we ate for breakfast!
meal = "An english muffin"

# Printing out breakfast
print("Breakfast:")
print(meal)

# Now update meal to be lunch!
meal = "burrito"

# Printing out lunch
print("Lunch:")
print(meal)

# Now update "meal" to be dinner
meal = "pasta"
# Printing out dinner
print("Dinner:")
print(meal)



#The + operator doesn’t just add two numbers, it can also “add” two strings!
# The process of combining two strings is called string concatenation.
# Performing string concatenation creates a brand new string comprised of
# the first string’s contents followed by the second string’s contents
# (without any added space in-between).


greeting_text = "Hey there!"
question_text = "How are you doing?"
full_text = greeting_text + question_text

# Prints "Hey there!How are you doing?"
print(full_text)

full_text = greeting_text + " " + question_text

# Prints "Hey there! How are you doing?"
print(full_text)




#If you want to concatenate a string with a number you will need to make the number a string first,
# using the str() function. If you’re trying to print() a numeric variable you can use commas to pass it
# as a different argument rather than converting it to a string.

birthday_string = "I am "
age = 10
birthday_string_2 = " years old today!"

# Concatenating an integer with strings is possible if we turn the integer into a string first
full_birthday_string = birthday_string + str(age) + birthday_string_2

# Prints "I am 10 years old today!"
print(full_birthday_string)

# If we just want to print an integer
# we can pass a variable as an argument to
# print() regardless of whether
# it is a string.

# This also prints "I am 10 years old today!"
print(birthday_string, age, birthday_string_2)





#Python offers a shorthand for updating variables.
# When you have a number saved in a variable and want to add to the current value of the variable,
# you can use the += (plus-equals) operator.

# First we have a variable with a number saved
number_of_miles_hiked = 12

# Then we need to update that variable
# Let's say we hike another two miles today
number_of_miles_hiked += 2

# The new value is the old value
# Plus the number after the plus-equals
print(number_of_miles_hiked)
# Prints 14

#The plus-equals operator also can be used for string concatenation, like so:

hike_caption = "What an amazing time to walk through nature!"

# Almost forgot the hashtags!
hike_caption += " #nofilter"
hike_caption += " #blessed"

#We create the social media caption for the photograph of nature we took on our hike,
# but then update the caption to include important social media tags we almost forgot.




#Python strings are very flexible, but if we try to create a string that occupies multiple lines
# we find ourselves face-to-face with a SyntaxError. Python offers a solution: multi-line strings.
# By using three quote-marks (""" or ''') instead of one,
# we tell the program that the string doesn’t end until the next triple-quote.
# This method is useful if the string being defined contains a lot of quotation marks and
# we want to be sure we don’t close it prematurely.

leaves_of_grass = """
Poets to come! orators, singers, musicians to come!
Not to-day is to justify me and answer what I am for,
But you, a new brood, native, athletic, continental, greater than
  before known,
Arouse! for you must justify me.
"""
