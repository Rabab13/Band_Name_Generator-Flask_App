print("Welcome to the Band Name Generator.")
# The input() function is a built-in function in Python that allows you to read a line of text from the user's input and return it as a string. The string argument passed to the input() function is used as the prompt to the user. In this case, the user is asked to enter the name of the city they grew up in. The user's input is then stored in the street variable, which can be used later in the program.
street = input("What's the name of the city you grew up in?\n")
band_name = "The "+input(f"Okay, so {street} is where you grew up. What would you like your band to be called?\n")
band_name = "The "+street.capitalize()+" Rebels\n"
#Adding The and .capitalize() for proper capitalization

pet = input("What's your pet's name?\n")
print("Your band name could be " + street + " " + pet)