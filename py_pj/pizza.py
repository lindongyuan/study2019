'''
def make_pizza(*toppings):
    #打印顾客点的所有配料
    print("\nmaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')
'''

def make_pizza(size,*toppings):
    print("\nMaking a " + str(size) +
          "-inch pizza with the floowing toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')