"""Last week you wrote a program that processed a collection of temperature readings
entered by the user and displayed the maximum, minimum, and mean. Create a
version of that program that takes the values from the command-line instead. Be
sure to handle the case where no arguments are provided!"""

import sys

temps = sys.argv[1:]


if temps:
   
    temps = [float(temp) for temp in temps]
    
    
    max_temp = max(temps)
    min_temp = min(temps)
    mean_temp = sum(temps) / len(temps)
    
  
    print(f"Maximum temperature: {max_temp}")
    print(f"Minimum temperature: {min_temp}")
    print(f"Mean temperature: {mean_temp:.2f}")
else:
    print("No temperature values provided.")
