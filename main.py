#functions printing and returning
#print something in a function, its only for displaying
# some data, you are doing nothing with the data

# when you return in a function, you are going to use it
# in another part of your program 
from addfruit import add_fruit
from divide_Fruit import divide_fruit
from subtract_fruit import subtract_fruit
from displayFruit import display_fruit

apples = int(input("How many apples?"))
oranges = int(input("How many oranges?"))

#add fruit
# When ever you return items, you must put the
# returned value inside of a variable
fruitAdded = add_fruit(apples,oranges)
print(fruitAdded)
# #subtract fruit
sub = subtract_fruit(apples,oranges)
print(sub)
# #divide fruit
div = divide_fruit(apples,oranges)
print(div)
# #disply the added fruit, subtracted fruit, and divided fruit
# create another file called display fruit 
display_fruit(fruitAdded, sub, div)