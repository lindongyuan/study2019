def make_pizza(size,*toppings):
    '''概述需要制作的pizza'''
    print("\nMaking a " + str(size) +"-inch pizza with the fllowing toppings:")
    for topping in toppings:
        print("- " + topping)