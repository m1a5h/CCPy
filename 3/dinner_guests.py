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
guests.remove(busy)

print(f"Sadly, {busy} cannot make it :(")
