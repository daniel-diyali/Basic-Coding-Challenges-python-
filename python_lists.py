# Create a function that appends user input values into a list.
# Create a list of your favorite animals, then sort the list alphabetically.

listOfColors =  []

for x in range(0, 3):
    color = input("Enter a color: ")
    listOfColors.append(color)

listOfColors.sort()
print(listOfColors)