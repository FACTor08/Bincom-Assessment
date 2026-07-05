from collections import Counter
from random import randint
import statistics

colours = [
    #MONDAY:
    "GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "BLUE", "YELLOW", "ORANGE", "CREAM", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN",
    #TUESDAY:
     "ARSH", "BROWN", "GREEN", "BROWN", "BLUE", "BLUE", "BLEW", "PINK", "PINK", "ORANGE", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "WHITE", "BLUE", "BLUE", "BLUE",
    #WEDNESDAY:
    "GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "RED", "YELLOW", "ORANGE", "RED", "ORANGE", "RED", "BLUE", "BLUE", "WHITE", "BLUE", "BLUE", "WHITE", "WHITE",
    #THURSDAY:
    "BLUE", "BLUE", "GREEN", "WHITE", "BLUE", "BROWN", "PINK", "YELLOW", "ORANGE", "CREAM", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN",
    #FRIDAY
    "GREEN", "WHITE", "GREEN", "BROWN", "BLUE", "BLUE", "BLACK", "WHITE", "ORANGE", "RED", "RED", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "WHITE"
]
colours = [c.replace("ARSH", "ASH").replace("BLEW", "BLUE") for c in colours]

count = Counter(colours)

sort_colours = count.most_common()
#The most occuring colours from high to low(frequency)
print("Colour frequency: ", sort_colours)

# Count for each colour
frequencies = [item[1] for item in sort_colours]

# Mean (average frequency per color)
mean = sum(frequencies) / len(frequencies)
print("Mean:", mean)

# Variance (how spread out the frequencies are from the mean)
variance = statistics.variance(frequencies)
print("Variance:", variance)

#Finding the most worn colour
mode = sort_colours[0][0]
print("The most worn colour is:", mode)

#Median colour
median_index = len(sort_colours)//2
median = sort_colours[median_index][0]
print(median)

#Question 8
#Generating Random 4 digit binary number
binary_digits = [str(randint(0,1)) for i in range(4)]
binary_number = "".join(binary_digits)
print("binary digits:", binary_number)

#Converting to base 10
denary_number = int(binary_number, 2)
print("Binary digits in base 10 is:", denary_number)

#Question 9 
#Sum of first 50 fibonacci sequence
sequence = [0,1]
for i in range(2,50):
    next = sequence[-1] + sequence[-2]
    sequence.append(next)
total_sum = sum(sequence)   
print(total_sum)   