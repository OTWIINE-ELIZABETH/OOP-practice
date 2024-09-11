

# Class: Vehicle
class Vehicle:
    # Attributes: make, model, year
    def __init__(self, make, model, year):
        # Initialize attributes
        self.make = make
        self.model = model
        self.year = year

    # Method: start_engine()
    def start_engine(self):
        # Print a message indicating the engine is started
        print("Engine started")