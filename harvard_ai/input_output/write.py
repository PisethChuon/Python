# Adds to the end without deleting existing content
with open("example.txt", "a") as file:
    file.write("\nThis line is added at the end.\n")

with open("example.txt") as file:
    print(file.read())