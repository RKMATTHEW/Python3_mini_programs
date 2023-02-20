#An integer, or int, is a whole number.
#A floating-point number, or a float, is a decimal number

an_int = 2
a_float = 2.1

print(an_int + 3)
# Output: 5

#We call the number 3 here a literal, meaning it’s actually the number 3
# and not a variable with the number 3 assigned to it.



#Python performs the arithmetic operations of addition, subtraction, multiplication, and division with +, -, *, and /

# Prints "500"
print(573 - 74 + 1)

# Prints "50"
print(25 * 2)

# Prints "2.0"
print(10 / 5)

#Notice that when we perform division, the result has a decimal place.
# This is because Python converts all ints to floats before performing division.

#the following are practice

int_2 = 23

float_2 = 25.2

print(int_2 + float_2)



#You’ve decided to get into quilting! To calculate the number of squares you’ll need for your first quilt
# let’s create two variables: quilt_width and quilt_length.
# Let’s make this first quilt 8 squares wide and 12 squares long.
#Print out the number of squares you’ll need to create the quilt!
#It turns out that quilt required a little more material than you have on hand!
# Let’s only make the quilt 8 squares long. How many squares will you need for this quilt instead?

quilt_width = 8

quilt_length = 12

print(quilt_width * quilt_length)

quilt_length = 8

print(quilt_width * quilt_length)

#We create two variables and assign numeric values to them. Then we perform a calculation on them.
#This doesn’t update the variables! When we update the quilt_length variable and perform the calculations again,
# they use the updated values for the variable!



#Python can also perform exponentiation. In written math, you might see an exponent as a superscript number,
# but typing superscript numbers isn’t always easy on modern keyboards.
# Since this operation is so related to multiplication, we use the notation **

# 2 to the 10th power, or 1024
print(2 ** 10)

# 8 squared, or 64
print(8 ** 2)

# 9 * 9 * 9, 9 cubed, or 729
print(9 ** 3)

# We can even perform fractional exponents
# 4 to the half power, or 2
print(4 ** 0.5)
