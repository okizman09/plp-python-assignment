class Smartphone:
    def __init__(self, brand, model, battery_life):
        #Defines A class with certain attributes
        self.brand = brand
        self.model = model
        self.battery_life =battery_life
    

    def call(self, number):
        #Defines a function to call using the number object
        print(f"Calling {number}.....")


    def charge(self, amount):
        #Defines a function to charge 
        self.battery_life += amount
        print(f"Battery charged to {self.battery_life}%")



    def show_details(self):
        print(f"{self.brand} {self.model}, Battery: {self.battery_life}%")        



class Smartphonepro(Smartphone):
    def take_photo(self, resolution):
        print(f"Taking a photo with a {resolution} camera.")
