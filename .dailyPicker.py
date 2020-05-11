# This script finds a semi-random combination of GTK and Icon theme to be used every day.

# Importing the random module so that we can make random numbers.
import random
for x in range(1):
    i = random.randint(0, 13)  # Finding a random number for the icons

for x in range(1):
    n = random.randint(0, 9)  # Finding a random number for the themes

themes = [
    'Bazik',
    'Materia-Purple',
    'Nordic',
    'Pop',
    'Flat-Green',
    'Vimix',
    'Yaru',
    'Mojave',
    'Qogir',
    'Prof-GNOME']  # Listing all the themes we have to choose from

icons = [
    'Flatery',
    'Marwaita',
    'Numix',
    'Numix Circle',
    'Oranchelo',
    'Paper',
    'Papirus',
    'Tela',
    'Tela Circle',
    'Vimix',
    'Vitas',
    'Zafiro',
    'Candy',
    'Mojave']  # Listing all the icons we have to choose from

chosenIcon = icons[i]  # This variable is the chosen icon theme
chosenTheme = themes[n]  # This variable is the chosen GTK theme

if chosenTheme == 'Nordic':
    # The Nordic theme only goes with the Zafiro icon set, so we override the computer's choice of icons if the chosen theme is Nordic.
    chosenIcon = 'Zafiro'

if chosenTheme == 'Qogir':
    # The Qogir icon theme only goes with the Qogir GTK theme, so if the Qogir GTK theme gets selected, the Qogir icons will accompany.
    chosenIcon = 'Qogir'

while chosenTheme == 'Pop' and chosenIcon == 'Zafiro':
    for x in range(1):
        i = random.randint(0, 14)

    for x in range(1):
        n = random.randint(0, 8)

    chosenIcon = icons[i]
    # Pop and Zafiro don't go well together, so we redo the random selection process as long as they are the chosen pair. This can be expanded in the future.
    chosenTheme = themes[n]

while chosenTheme == 'Yaru' and chosenIcon == 'Zafiro':
    for x in range(1):
        i = random.randint(0, 14)

    for x in range(1):
        n = random.randint(0, 8)

    chosenIcon = icons[i]
    # Yaru and Zafiro don't go well together, so we redo the random selection process as long as they are the chosen pair. This can be expanded in the future.
    chosenTheme = themes[n]

# Creating a nice human-readable string.
outputThemes = "Today's GTK and Shell Theme: " + chosenTheme
# Creating a nice human-readable string
outputIcons = "Today's Icon Theme: " + chosenIcon

toDo = ''' 
Nothing outstanding!
'''
# Insert the list of things to do here

toDoFinal = "Things to do soon: " + toDo  # Create the todo string to be output

print(outputThemes)
print(outputIcons)  # Printing the results
print()  # Empty line
print(toDoFinal)  # Print the things I have to do
