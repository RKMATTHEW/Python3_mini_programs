#Examine the existing list heights in your code editor.

#A new student just joined the class!

#Chloe is 65 inches tall

#Add Chloe’s height to the end of the list heights.

heights = [61, 70, 67, 64, 65]

broken_heights = [65, 71, 59, 62]







#Add any additional string to the end of the list ints_and_strings.

#Create a new list called sam_height_and_testscore that contains:

#The string "Sam" (to represent Sam’s name)
#The number 67 (to represent Sam’s height)
#The float 85.5 (to represent Sam’s score)
#The boolean True (to represent Sam passing the test)
#Make sure to write the elements in exact order.

ints_and_strings = [1, 2, 3, "four", "five", "six"]

sam_height_and_testscore = ["Sam", 67, 85.5, True]






#Jiho works for a gardening store called Petal Power. Jiho keeps a record of orders in a list called orders.

#Use print to inspect the orders he has received today.

#Jiho just received a new order for "tulips". Use append to add this string to orders.

#Another order has come in! Use append to add "roses" to orders.

#Use print to inspect the orders Jiho has received today.

orders = ["daisies", "periwinkle"]

print(orders)

orders.append("tulips")

orders.append("roses")

print(orders)








#Jiho is updating a list of orders. He just received orders for "lilac" and "iris".

#Create a list called new_orders that contains our new orders.

#Use + to create a new list called orders_combined that combines orders with new_orders.


orders = ["daisy", "buttercup", "snapdragon", "gardenia", "lily"]

# Create new orders here:

new_orders = ["lilac", "iris"]

orders_combined = orders + new_orders

broken_prices = [5, 3, 4, 5, 4] + [4]



#Use square brackets ([ and ]) to select the 4th employee from the list employees. Save it to the variable employee_four.

#Checkpoint 2 Passed

#Stuck? Get a hint

#2.Paste the following code into script.py:

#print(employees[8])
#What happens? Why?

employees = ["Michael", "Dwight", "Jim", "Pam", "Ryan", "Andy", "Robert"]

employee_four = employees[3]
print(employees[4])


#Create a variable called last_element.

#Assign the last element in shopping_list to the variable last_element using a negative index.


#2.Now select the element with index 5 and save it to the variable index5_element.

#3.Use print to display both index5_element and last_element.

#Note that they are equal to "cereal"!

shopping_list = ["eggs", "butter", "milk", "cucumbers", "juice", "cereal"]

last_element = shopping_list[-1]

index5_element = shopping_list[5]

print(last_element)

print(index5_element)