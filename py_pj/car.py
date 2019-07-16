class Car():
    '''一次模拟汽车的简单尝试'''

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 21

    def get_descriptive_name(self):
        '''返回整洁的描述性信息'''
        long_name = str(self.year) +" " +self.make + " "+ self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    '''通过方法修改属性的值'''
    #mileage = 25
    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self,miles):
        '''将里程表计数增加指定的量'''
        self.odometer_reading += miles

my_new_car = Car('audi','a4','2016')
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reding = 23
my_new_car.read_odometer()

my_new_car.update_odometer(25)
my_new_car.read_odometer()

my_user_car = Car('subaru','outback','2013')
print(my_user_car.get_descriptive_name())

my_user_car.update_odometer(23500)
my_user_car.read_odometer()

my_user_car.increment_odometer(100)
my_user_car.read_odometer()




