import unittest
import json
from read_animals import read_head

class TestReadAnimal(unittest.TestCase):

	def test_read_head(self):
		self.assertEqual(read_head(animal_list, 'snake', 1), animal_list['animals'][0])
		self.assertEqual(read_head(animal_list, 'snake', 2), animal_list['animals'][5])
		self.assertEqual(read_head(animal_list, 'snake', 146), 'There are only 6 animals with a snake head.')

if __name__ == '__main__':
	with open('animals.json', 'r') as f:
		animal_list = json.load(f)
	unittest.main()

