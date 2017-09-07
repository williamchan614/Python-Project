import random


def welcome():
	print("IO training v1.1")
	print("r - review words")
	print("e - enter words")
	print("d - delete existing words")
	print("o - opens options")
	print("q - exits program")

def ask():
	return raw_input("Enter a command: ")

def review(file):
	info = file.readlines()
	lines = len(info)
	if info == []:
		print("You have no words saved")
		return None
	index_of_word = random.randrange(0,lines,2)
	word = info[index_of_word]
	definition = info[index_of_word+1]

	print(definition)
	return word



def enter(name):
	file = open(name,"a")
	print("type q anytime to cancel")
	while(True):
		word = raw_input("Please enter a word")
		definition = raw_input("Please define it")
		if word == 'q' or definition == 'q':
			break
		file.write(word)
		file.write(definition)


def delete(name):
	file = open(name,"r")
	info = file.readlines()
	file.close()
	if info == []:
		print("You have no words saved")
		return None
	word = raw_input("Enter the word to delete")
	file = open(name,"w")
	for line in info:
		if line != word:
			file.write(line)
	
	

def options():
	None




