"""2. Write a program that prompts a user to enter a temperature in Celsius, and then
displays the corresponding temperature in Fahrenheit, like so:
Enter a temperature in Celsius: 32.5
32.5C is equivalent to 90.5F."""

celsius = float(input("Enter a temperature in Celsius: "))
fahreinheit = (celsius * 9 / 5) + 32
print(celsius,"C is equivalent to",fahreinheit,"F")