"""8. Modify the previous program so that it can process any number of values. The input
terminates when the user just pressed "Enter" at the prompt rather than entering a
value."""

import statistics

def get_temperatures():
    temperatures = []
    while True:
        temp_value = input(f"Enter temperature or press Enter to finish: ")
        
        if temp_value == "":
            break
        else:
            temperatures.append(float(temp_value))
    
    return temperatures

def calculate_max(temperatures):
    return max(temperatures)

def calculate_min(temperatures):
    return min(temperatures)

def calculate_mean(temperatures):
    return statistics.mean(temperatures)

def temperature():
    temperatures = get_temperatures()

    if len(temperatures) == 0:
        print("Error! No temperature were entered.")
        return
    else:
        maximum_temperature = calculate_max(temperatures)
        minimum_temperature = calculate_min(temperatures)
        mean_temperature = calculate_mean(temperatures)

        print()
        print("Maximum temperature: " , maximum_temperature)
        print("Minimum temperature: ", minimum_temperature)
        print("Mean temperature: ", mean_temperature)

temperature()
