#!/usr/bin/env python

food = ["Apples", "Pears", "Oranges", "Peaches"]

print food

new_food = raw_input(u'choose a your favorite fruit to add to the list')

m = new_food

food.append(m)

print food

number = raw_input(u'Pick a number.')

#int is required otherwise food[] causes error
#error message expecting integer

n = int(number)

print food[n]

new_fruit = raw_input(u'choose an other fruit')

j = new_fruit

food.insert(0, j)
print food
"""Iknow assignment wanted me to do this with the
'+' when i tried i kept getting errors so I only used
.insert()"""

#fuction returning furits starting with P here

print food
#remove last fruit in food list
food1 = food
food1.pop()
print food1

delete_fruit = raw_input(u'choose a fruit to remove from list')
d = delete_fruit
food1.remove(d)





