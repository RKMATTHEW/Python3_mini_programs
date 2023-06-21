#We are helping out a popular grocery store called Jiho’s Produce.

#Every week the store has to choose the order in which it displays some of its popular items on sale in the front window to attract customers.

#Jiho, the store owner, likes to store the items for the display in a list.

#Check out the current display list in our code editor. Click Run to print out the list.

#Jiho found out some great news! "Pineapple" is back in stock.

#Jiho would like to put "Pineapple" in the front of the list so it is the first item customers see in the display window.

#Use .insert() to add "Pineapple" to the front of the list.

#Print the resulting list to see the change.

#Note: For this list, the front will be the element at index 0

front_display_list = ["Mango", "Filet Mignon", "Chocolate Milk"]
print(front_display_list)

# Your code below:
front_display_list.insert(0, "Pineapple")

print(front_display_list)




#We have decided to pursue the study of data science in addition to our computer science coursework. We signed up for an online school that would help us become proficient.

#Check out the current list of topics we will be studying in our code editor.

#Click Run to print out the list.

#It looks like we have an overlap with our computer science curriculum for the topic of "Python 3".

#Let’s remove the topic from the list of data_science_topics using our newly learned .pop() method.

#Print data_science_topics to see your result.

#Looks like there is overlap on the "Algorithms" topic as well. Let’s use .pop() to remove it as well.

#Print data_science_topics to see the changes.

data_science_topics = ["Machine Learning", "SQL", "Pandas", "Algorithms", "Statistics", "Python 3"]
print(data_science_topics)

# Your code below:
data_science_topics.pop()

print(data_science_topics)

data_science_topics.pop(3)

print(data_science_topics)






#Modify number_list so that it is a range containing numbers starting at 0 and up to, but not including, 9.

#Create a range called zero_to_seven with the numbers 0 through 7.

#Print the result in list form.


number_list = range(9)
print(list(number_list))

zero_to_seven = range(8)

print(list(zero_to_seven))







#Modify the range() function that created the range range_five_three such that it:

#Starts at 5
#Has a difference of 3 between each item
#Ends before 15

#Create a range called range_diff_five that:

#Starts at 0
#Has a difference of 5 between each item
#Ends before 40


range_five_three = range(5, 15, 3)

range_diff_five = range(0, 40, 5)








#Calculate the length of long_list and save it to the variable long_list_len.

#Use print() to examine long_list_len.

#We have provided a completed range() function for the variable big_range.

#Calculate its length using the function len() and save it to a variable called big_range_length.

#Note: Range objects do not need to be converted to lists in order to determine their length

#Use print() to examine big_range_length.

#Change the range() function that generates big_range so that it skips 100 instead of 10 steps between items.

#How does this change big_range_length?


long_list = [1, 5, 6, 7, -23, 69.5, True, "very", "long", "list", "that", "keeps", "going.", "Let's", "practice", "getting", "the", "length"]

big_range = range(2, 3000, 100)

# Your code below:
long_list_len = len(long_list)

print(long_list_len)

big_range_length = len(big_range)

print(big_range_length)








#Use print() to examine the variable beginning.

#Before hitting Run think about what elements beginning will contain?

#Modify beginning, so that it selects the first 2 elements of suitcase.

#Create a new list called middle that contains the middle two items ( ["pants", "pants"] ) from suitcase.

#Print middle to see the slice!

suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

beginning = suitcase[0:2]

# Your code below:
print(beginning)

middle = suitcase[2:4]

print(middle)








#Create a new list called last_two_elements containing the final two elements of suitcase.

#Print last_two_elements to see your result.


#Create a new list called slice_off_last_three containing all but the last three elements.

#Print slice_off_last_three to see your result.

suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

# Your code below:
last_two_elements = suitcase[-2:]

print(last_two_elements)

slice_off_last_three = suitcase[:-3]

print(slice_off_last_three)









#Mrs. Wilson’s class is voting for class president. She has saved each student’s vote into the list votes.

#Use .count() to determine how many students voted for "Jake" and save the value to a variable called jake_votes.

#Use print() to examine jake_votes.

votes = ["Jake", "Jake", "Laurie", "Laurie", "Laurie", "Jake", "Jake", "Jake", "Laurie", "Cassie", "Cassie", "Jake", "Jake", "Cassie", "Laurie", "Cassie", "Jake", "Jake", "Cassie", "Laurie"]

# Your code below:

# Checkpoint 1
jake_votes = votes.count("Jake")

# Checkpoint 2
print(jake_votes)















#Use .sort() to sort addresses.

#Use print() to see how addresses changed.

#Remove the # and whitespace in front of the line sort(names). Edit this line so that it runs without producing a NameError.

#Use print to examine sorted_cities. Why is it not the sorted version of cities?

#Edit the .sort() call on cities such that it sorts the cities in reverse order (descending).

#Print cities to see the result.


# Checkpoint 1 & 2
addresses = ["221 B Baker St.", "42 Wallaby Way", "12 Grimmauld Place", "742 Evergreen Terrace", "1600 Pennsylvania Ave", "10 Downing St."]
addresses.sort()
print(addresses)


# Checkpoint 3
names = ["Ron", "Hermione", "Harry", "Albus", "Sirius"]
names.sort()


# Checkpoint 4 & 5
cities = ["London", "Paris", "Rome", "Los Angeles", "New York"]
sorted_cities = cities.sort(reverse=True)
print(sorted_cities)
print(cities)