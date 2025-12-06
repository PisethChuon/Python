class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} , {self.brand} , {self.model}")

    def start_engine(self):
        print("The engine has started.")
        
car = Car("Toyota", "Corolla", 2020)
car.display_info()
car.start_engine()