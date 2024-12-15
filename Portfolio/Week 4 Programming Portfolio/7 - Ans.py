"""7. Write a program that reads 6 temperatures (in the same format as before), and
displays the maximum, minimum, and mean of the values.
Hint: You should know there are built-in functions for max and min. If you hunt, you
might also find one for the mean."""

import statistics

def get_temperatures():
    temperatures = []
    for i in range(6):
        temp_value = float(input(f"Enter temperature {i + 1}: "))
        temperatures.append(temp_value)
    return temperatures

def calculate_max(temperatures):
    return max(temperatures)

def calculate_min(temperatures):
    return min(temperatures)

def calculate_mean(temperatures):
    return statistics.mean(temperatures)

def temperature():
    temperatures = get_temperatures()
    
    maximum_temperature = calculate_max(temperatures)
    minimum_temperature = calculate_min(temperatures)
    mean_temperature = calculate_mean(temperatures)

    print()
    print("Maximum temperature: " , maximum_temperature)
    print("Minimum temperature: ", minimum_temperature)
    print("Mean temperature: ", mean_temperature)

temperature()
