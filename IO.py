import os
import fx
import random


os.chdir("/Users/rou/Documents")




def welcome():
	print("IO training v1.1")
	print("r - review words")
	print("e - enter words")
	print("d - delete existing words")
	print("o - opens options")
	print("q - exits program")

def ask():
	return input("Enter a command: ")

def review(file):
	info = file.readlines()
	lines = len(info)
	if info == []:
		print("You have no words saved")
		return None
	index_of_word = random.randrange(0,lines-1,2)
	word = info[index_of_word]
	definition = info[index_of_word+1]

	print(definition)
	return word



def enter(name):
	file = open(name,"a")
	print("type q anytime to cancel")
	while(True):
		word = input("Please enter a word ")
		if word == 'q':
			break
		definition = input("Please define it ")
		if definition == 'q':
			break
		file.write(word+"\n")
		file.write(definition+"\n")


def delete(name):
	file = open(name,"r")
	info = file.readlines()
	file.close()
	if info == []:
		print("You have no words saved")
		return None


	word = input("Enter the word to delete")
	word = word+'\n'
	file = open(name,"w")
	saw = False
	for line in info:
		if saw == True:
			saw = False
			continue

		if line != word:
			file.write(line)

		else:
			saw = True
	
	

def options():
	None



name = "save.txt"

if not os.path.exists(name):
	file = open(name,"w+")
if not os.path.exists("settings.txt"):
	settings = open("settings.txt","w+")
	settings.write("")

file = open(name,"r+")
settings = open("settings.txt","r+")

count = int(len(file.readlines())/2)



welcome() #Welcome banner
while(True):
	file = open(name,"r+")
	choice = ask() #Ask if the user wants to enter words or review
	if choice == "r":
		for i in range(count): #keep looping until user exits by typing q
			file = open(name,"r+")
			word = review(file)
			if word == None:
				break
			word = word.lower().strip()
			reponse = input("Word:").lower()
			if reponse == 'q':
				break
			if word != reponse:
				print("Incorrect, word was",word)
				continue
			file.close()


	elif choice == "e":
		enter(name)
		count = int(len(file.readlines())/2)
		file.close()
	elif choice == "d":
		delete(name)
		count = int(len(file.readlines())/2)
		file.close()
	elif choice == "o":
		options()
		file.close()
	elif choice == "q":
		exit()
	else:
		print("Please enter a valid input")





'''
file = open("save.txt","r+")
info = file.readlines()
if info == []:
	file.write("Example:A definition.")
	print("Loading")
else:
	print((info[0].split(":"))[1])
file.close()
'''