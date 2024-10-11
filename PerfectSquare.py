import math

# Creating A List
Numbers = [4, 16, 17, 11, 36, 82, 
		81, 49, 110, 120, 100]

# Printing the original array
print("The original List is : ", Numbers)

# Using List comprehension to find perfect squares
perfect_squares = [i for i in Numbers if (
	math.sqrt(i) == math.floor(math.sqrt(i)))]

# Printing the perfect squares
print("The perfect squares are: ", perfect_squares)
