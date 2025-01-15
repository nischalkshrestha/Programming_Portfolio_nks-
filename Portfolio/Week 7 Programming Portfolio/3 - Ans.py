"""Write a program that manages a list of countries and their capital cities. It should
prompt the user to enter the name of a country. If the program already "knows"
the name of the capital city, it should display it. Otherwise it should ask the user to
enter it. This should carry on until the user terminates the program (how this
happens is up to you)."""

def manage_countries():
    country_capitals = {}
    
    print("Welcome to the Country-Capital Manager!")
    print("Enter 'exit' as the country name to terminate the program.")
    
    while True:
        country = input("\nEnter the name of a country: ").strip()
        
        if country.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break
        
        if country in country_capitals:
            print(f"The capital of {country} is {country_capitals[country]}.")
        else:
            capital = input(f"I don't know the capital of {country}. Please enter it: ").strip()
            country_capitals[country] = capital
            print(f"Thank you! I've added {country} with its capital {capital} to my list.")
    
    print("\nHere is the list of countries and their capitals you entered:")
    for country, capital in country_capitals.items():
        print(f"{country}: {capital}")


manage_countries()
