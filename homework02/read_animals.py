import json
import random
import argparse

head_list = ['snake', 'bull', 'lion', 'raven', 'bunny']

def check_head(head):
	if head not in head_list:
		raise argparse.ArgumentTypeError('%s is not a valid head shape.'  % head)
	return(head)

def check_positive(value):
	ivalue = int(value)
	if ivalue <=0:
		raise argparse.ArgumentTypeError('%s is an invalid positive integer.' % value)
	return ivalue

parser = argparse.ArgumentParser(description='Pulls an animal from the animal list. Pulls a random animal by default.')
parser.add_argument('-H', '--head_shape', type=check_head,  metavar='',  help='Selects the head shape of the pulled animal')
parser.add_argument('-i', '--index_number', type=check_positive, default=0, metavar='', help='Selects what index to pull from the animal list, relative to the head shape, if specified. Must be 1 or greater.')

args = parser.parse_args()

def read_random(animal_list):
	print(animal_list['animals'][random.randint(0,19)])

def read_specified(animal_list, index):
	max=len(animal_list['animals'])
	if index > max:
		print('There are only %s animals on the list' % max)
		return
	print(animal_list['animals'][(index-1)])

def read_head(animal_list, head_shape, index_number):
	num = 0
	for i in animal_list['animals']:
		if(i['head'] == head_shape) and (num >= (index_number-1)):
			return(i)
		elif(i['head'] == head_shape):
			num += 1
	return(('There are only %s animals with a %s head.' % ((num+1), head_shape)))

if __name__ == '__main__':
	with open('animals.json', 'r') as f:
		animal_list = json.load(f)
	if args.index_number==0 and args.head_shape==None:
		read_random(animal_list)
	elif args.head_shape==None:
		read_specified(animal_list, args.index_number)
	else:
		print(read_head(animal_list, args.head_shape, args.index_number))
