#This script finds a semi-random combination of GTK and Icon theme to be used every day.

import random #Importing the random module so that we can make random numbers.
for x in range(1):
  i = random.randint(0,13) #Finding a random number for the icons

for x in range(1):
  n = random.randint(0,8) #Finding a random number for the themes

themes = [
'Bazik',
'Materia-Purple',
'Nordic',
'Pop',
'Flat-Green',
'Vimix',
'Yaru',
'Mojave',
'Prof-GNOME'] #Listing all the themes we have to choose from

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
'Mojave'] #Listing all the icons we have to choose from

chosenIcon = icons[i] #This variable is the chosen icon theme
chosenTheme = themes[n] #This variable is the chosen GTK theme

if chosenTheme == 'Nordic':
 chosenIcon = 'Zafiro' #The Nordic theme only goes with the Zafiro icon set, so we override the computer's choice of icons if the chosen theme is Nordic.

while chosenTheme == 'Pop' and chosenIcon == 'Zafiro':
  for x in range(1):
    i = random.randint(0,14)

  for x in range(1):
    n = random.randint(0,8)

  chosenIcon = icons[i]
  chosenTheme = themes[n] #Pop and Zafiro don't go well together, so we redo the random selection process as long as they are the chosen pair. This can be expanded in the future.

while chosenTheme == 'Yaru' and chosenIcon == 'Zafiro':
  for x in range(1):
    i = random.randint(0,14)

  for x in range(1):
    n = random.randint(0,8)

  chosenIcon = icons[i]
  chosenTheme = themes[n] #Yaru and Zafiro don't go well together, so we redo the random selection process as long as they are the chosen pair. This can be expanded in the future.

outputThemes = "Today's GTK and Shell Theme: " + chosenTheme #Creating a nice human-readable string.
outputIcons = "Today's Icon Theme: " + chosenIcon #Creating a nice human-readable string

print(outputThemes)
print(outputIcons) #Printing the results