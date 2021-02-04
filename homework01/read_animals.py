import json
import random

with open('animals.json', 'r') as f:
	animalList = json.load(f)

print(animalList['animals'][random.randint(0,19)])
