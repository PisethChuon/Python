rows = int(input("Enter Row: "))

def print_pattern(rows):
    for r in range(1, rows + 1):
        for c in range(1, r + 1):
            print("*", end=" ")
        print()
    
print(print_pattern(rows))
