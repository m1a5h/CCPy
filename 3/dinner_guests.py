#!/usr/bin/python3

import random


guests = [
    "Archimedes",
    "Jesus",
    "Grothendieck",
    "Trotsky"
    ]

for guest in sorted(guests):
    print(f"I would like {guest} to come to dinner")

busy = random.choice(guests)
space = guests.index(busy)
guests.remove(busy)
guests.insert(space, "Richey")

print(f"Sadly, {busy} cannot make it :(")
print(f"However {guests[space]} is taking their place!")
