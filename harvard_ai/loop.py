# While loop example
# i = 1

# while i < 6:
#     print(i)
#     i += 1
# else:
#     print("Loop ended, i is now:", i)
        
#  ask the user for a password until they get it right:

# def main():
#     number = get_number()
#     meow(number)

# def get_number():
#     while True:
#         n = int(input("Enter a number greater than 0: "))
#         if n > 0:
#             break
#     return n
    
# def meow(n):
#     for n in range(n):
#         print("Meow!")

# main()

# For loop example

for i in range(1, 6):
    i += 1
    if i == 3:
        continue
    print("Loop ended, i is now:", i)
