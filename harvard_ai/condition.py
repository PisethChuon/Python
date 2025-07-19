# if condistion
# x = (input("What's is x: "))
# y = (input("What's is y: "))

# if x > y or x < y:
#     print("x is not equal to y")
# else:
#     print("x is equal to y")


# and condition
# score = int(input("Enter your score: "))
# if score >= 90 and score <= 100:
#     print("You got an A")
# elif score >= 80 and score < 90:
#     print("You got a B")
# elif score >= 70 and score < 80:
#     print("You got a C")
# elif score >= 60 and score < 70:
#     print("You got a D")
# else:
#     print("You got an F")

# Parity

def main():
    x = int(input("What's x?: "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
main()