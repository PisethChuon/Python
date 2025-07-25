# Adds to the end without deleting existing content
with open("examples.txt", "x") as file:
    file.write("This file is newly created.")

# with open("example.txt") as file:
#     print(file.read())