# Unit 4 HW 1

'''Create a function called list_of_cubes(start). That function should make, and return, a list of the first 10 cubes beginning with start using list comprehension. Then print the values from each of those lists to the console. For example, list_of_cubes(5) would return

[125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744]'''
def list_of_cubes(start:int)->list:
    #                              5      15
    cubes = [i**3 for i in range(start,start+10)]
    return cubes


'''
Create a function called pizza_modifier(topping_list, new_topping) that allows a user to add a new topping to a list of toppings. The function should print the current toppings and print the toppings with the new topping added.'''
def pizza_modifier(topping_list,new_topping):
    print(topping_list)
    topping_list.append(new_topping)
    print(topping_list)
    return None

def main():
    print(list_of_cubes(5))
    list_of_toppings = ['cheese','ham']
    pizza_modifier(list_of_toppings[:],'pineapple') #[:] passes a copy of the list
    print(list_of_toppings)


if __name__ == "__main__":
    main()