# This script finds a semi-random combination of GTK and Icon theme to be used every day.

# Importing the random module so that we can make random numbers.
import random
for x in range(1):
    i = random.randint(0, 9)  # Finding a random number for the icons

for x in range(1):
    n = random.randint(0, 5)  # Finding a random number for the themes

themes = [
    'Materia-Purple',
    'Flat-Green',
    'Vimix',
    'Yaru',
    'Catalina',
    'Prof-GNOME']  # Listing all the themes we have to choose from

icons = [
    'Flatery',
    'Marwaita',
    'Numix Circle',
    'Oranchelo',
    'Papirus',
    'Tela Circle',
    'Vitas',
    'Zafiro',
    'Candy',
    'Catalina']  # Listing all the icons we have to choose from

chosenIcon = icons[i]  # This variable is the chosen icon theme
chosenTheme = themes[n]  # This variable is the chosen GTK theme

while chosenTheme == 'Yaru' and chosenIcon == 'Zafiro':
    for x in range(1):
        i = random.randint(0, 14)

    for x in range(1):
        n = random.randint(0, 8)

    chosenIcon = icons[i]
    # Yaru and Zafiro don't go well together, so we redo the random selection process as long as they are the chosen pair. This can be expanded in the future.
    chosenTheme = themes[n]

while chosenTheme == 'Catalina' and chosenIcon == 'Zafiro':
    for x in range(1):
        i = random.randint(0, 14)

    for x in range(1):
        n = random.randint(0, 8)

    chosenIcon = icons[i]
    # Catalina and Zafiro don't go well together, so we redo the random selection process as long as they are the chosen pair. This can be expanded in the future.
    chosenTheme = themes[n]

while chosenTheme == 'Prof-GNOME' and chosenIcon == 'Zafiro':
    for x in range(1):
        i = random.randint(0, 14)

    for x in range(1):
        n = random.randint(0, 8)

    chosenIcon = icons[i]
    # Prof-GNOME and Zafiro don't go well together, so we redo the random selection process as long as they are the chosen pair. This can be expanded in the future.
    chosenTheme = themes[n]

# Creating a nice human-readable string.
outputThemes = "Today's GTK and Shell Theme: " + chosenTheme
# Creating a nice human-readable string
outputIcons = "Today's Icon Theme: " + chosenIcon

print(outputThemes)
print(outputIcons)  # Printing the results
