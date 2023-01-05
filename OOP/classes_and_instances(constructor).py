class Car:

    def __init__(self, color, model, speed):
        self.color = color
        self.model = model
        self.speed = speed

    def show_details(self):
        print(
            f'Color: {self.color}\nSpeed: {self.speed}\nModel: {self.model}\n')


'''
Note we do not have to pass in the argument for 'self' parameter when any method inside a class.
The object that we instantiate is automatically passed in for the self parameter.
'''
car_1 = Car('red', 'E12', '12mph')
car_2 = Car('green', 'R14', '100mph')

car_1.show_details()
car_2.show_details()

# An alternative way to call a function:
Car.show_details(car_1)  # Call show_details for the instance 'car_1'

# If you leave the parenthesis off, when refering to the method, you will get the following output:
print(car_1.show_details)
# <bound method Car.show_details of <__main__.Car object at mem_location>>
