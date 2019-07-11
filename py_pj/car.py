class Car():
    '''一次模拟汽车的简单尝试'''

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reding = 21

    def get_descriptive_name(self):
        '''返回整洁的描述性信息'''
        long_name = str(self.year) +" " +self.make + " "+ self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reding) + " miles on it.")

    def update_odometer(self,mileage):
        if mileage >= self.odometer_reding:
            self.odometer_reding = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(selfs,miles):
        '''将里程读数增加指定的量'''
        self.odometer_reding += miles


my_user_car = Car('subaru','outback','2013')
print(my_user_car.get_descriptive_name())

my_user_car

my_new_car = Car('audi','a4','2016')
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(20)
my_new_car.read_odometer()