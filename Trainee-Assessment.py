from collections import Counter
from random import randint
import statistics
import psycopg2


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

#Feature 1
# Mean (average frequency per color)
mean = sum(frequencies) / len(frequencies)
print("Mean:", mean)

#Feature 2
#Finding the most worn colour
mode = sort_colours[0][0]
print("The most worn colour is:", mode)

#Feature 3
#Median colour
median_index = len(sort_colours)//2
median = sort_colours[median_index][0]
print(median)

#Feature 4
# Variance 
variance = statistics.variance(frequencies)
print("Variance:", variance)

#Feature 7
#Probability of Red
total_reds = count["RED"]
total_colours = len(colours)
red_probability = total_reds/total_colours
print (f"probability of red = {red_probability} == {red_probability * 100:.2f}%")

#Feature 8
#Generating Random 4 digit binary number
binary_digits = [str(randint(0,1)) for i in range(4)]
binary_number = "".join(binary_digits)
print("binary digits:", binary_number)

#Converting to base 10
denary_number = int(binary_number, 2)
print("Binary digits in base 10 is:", denary_number)

#Feature 9 
#Sum of first 50 fibonacci sequence
sequence = [0,1]
for i in range(2,50):
    next = sequence[-1] + sequence[-2]
    sequence.append(next)
total_sum = sum(sequence)   
print(total_sum)   

# Feature 6
# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="password",
    port="5432"
)
cur = conn.cursor()

# Create the table (only colour + frequency)
cur.execute("""
    CREATE TABLE IF NOT EXISTS colour_frequency (
        colour VARCHAR(50) PRIMARY KEY,
        frequency INTEGER
    )
""")

# Insert each colour and its count
for colour, frequency in count.items():
    cur.execute("""
        INSERT INTO colour_frequency (colour, frequency)
        VALUES (%s, %s)
        ON CONFLICT (colour) DO UPDATE SET frequency = EXCLUDED.frequency
    """, (colour, frequency))

# Save and close
conn.commit()
cur.close()
conn.close()

print("Colours and frequencies saved to PostgreSQL successfully!")

