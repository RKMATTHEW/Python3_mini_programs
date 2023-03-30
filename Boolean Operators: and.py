#Set the variables statement_one and statement_two equal to the results
# of the following boolean expressions:

#Statement one:

#(2 + 2 + 2 >= 6) and (-1 * -1 < 0)
#Statement two:

#(4 * 2 <= 8) and (7 - 1 == 6)

statement_one = (2 + 2 + 2 >= 6) and (-1 * -1 < 0)

statement_two = (4 * 2 <= 8) and (7 - 1 == 6)

#Let’s return to Calvin Coolidge’s Cool College. 120 credits aren’t the only graduation requirement
# , you also need to have a GPA of 2.0 or higher.
#Rewrite the if statement so that it checks to see if a student meets both requirements using an and statement.

#If they do, print the string:

#"You meet the requirements to graduate!"

credits = 120
gpa = 3.4

if credits >= 120 and gpa >= 2.0:
  print("You meet the requirements to graduate!")



#Set the variables statement_one and statement_two equal to the results of the following boolean expressions:

#Statement_one: not (4 + 5 <= 9)

#Statement two: not (8 * 2) != 20 - 4

statement_one = (4 + 5 <= 9)

statement_two = not (8 * 2) != 20 - 4

credits = 120
gpa = 1.8


#The registrar’s office at Calvin Coolidge’s Cool College has been so impressed with your work so far that they have another task for you.

#They want you to return to a previous if statement and add in several checks using and and not statements:

#If a student’s credits is not greater or equal to 120, it should print:
#"You do not have enough credits to graduate."
#If their gpa is not greater or equal to 2.0, it should print:
# "Your GPA is not high enough to graduate."

#If their credits is not greater than or equal to 120 and their gpa is not greater than or equal to 2.0, it should print:
#"You do not meet either requirement to graduate!"

if not credits >= 120:
  print("You do not have enough credits to graduate.")

if not gpa >= 2.0:
  print("Your GPA is not high enough to graduate.")

if not (credits >= 120) and not (gpa >= 2.0):
  print("You do not meet either requirement to graduate!")kjk