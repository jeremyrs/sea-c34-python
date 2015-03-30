#!/usr/bin/env python

food = ["Apples", "Pears", "Oranges", "Peaches"]

print food

new_food = raw_input(u'choose a your favorite fruit to add to the list')

m = new_food

food.append(m)

print food

number = raw_input(u'Pick a number.')
n = int(number)

print food[n]
