#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
animals = ('bear', 'bunny', 'dog', 'cat', 'velociraptor')

for pet in animals:
    print(pet)
    if pet == 'dog':
        continue
    if pet == 'bunny':
        break
        print(pet)

    else:
        print("that is all of the animals")


mylist = ("wine", "vodka", "beer", "blood", "cider")


for drink in range(4):
    print(drink)
