# Exception
# Basic exception handling in Python
# try:
    # Sth might crash
    # user_input = int(input("Enter a number: "))
    # number = 100 / user_input
# except:
    # code that run if crash
    # print("You can't divide by zero!")
# else:
    # code that run if no crash
    # print("The result is:", number)

# ATM withdrawal System

# class InsufficientFundsError(Exception):
#     pass

# balance = 1000

# def withdraw(amount):
#     if amount > balance:
#         raise InsufficientFundsError("Insufficient funds for this withdrawal.")
    
# try:
#     withdraw(1500)

# except InsufficientFundsError as e:
#     print("Transaction failed:", e)


# Login system

class LoginError(Exception):
    pass

def login(username, password):
    if username != "admin" or password != "password123":
        raise LoginError("Invalid username or password.")
    else: 
        print("Login successful!")
    
try:
    login("admin", "password123")

except LoginError as e:
    print(e)