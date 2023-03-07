#Now that we’ve added conditional statements to our toolkit for building control flow,
# let’s explore more ways to create boolean expressions. So far we know two relational operators,
# equals and not equals, but there are a ton (well, four) more: (>)greater than, (<)less than
#(>=) greater than or equal to, (<=) less than or equal to.

#Create an if statement that checks if x and y are equal, print the string below if so:
#"These numbers are the same"

x = 20
y = 20

if x == y:
  print("These numbers are the same")


#The nearby college, Calvin Coolidge’s Cool College (or 4C, as the locals call it) requires students
# to earn 120 credits to graduate.
#Write an if statement that checks if the student has enough credits to graduate. If they do, print the string:
#"You have enough credits to graduate!"

credits = 120

if credits >= 120:
  print("You have enough credits to graduate!")