height = input("Enter heights: ").split() # Splits the heights into an array
print(height)

index = 0
total_height = 0
for h in height:
    total_height += int(h)
    index += 1

average_height = total_height/index
print("Average Height: " + str(average_height))
