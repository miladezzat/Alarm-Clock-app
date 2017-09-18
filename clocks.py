from random import randint #import randint object from random model
import time #import time model
import webbrowser #import webbrowser model
class OurObject:  #name of our class

	def randomLink(self):  #methos one that produce random link from ourlist
		#when choice number one
		try:
			fhand = open('ourlist.txt','r') #open our List file
			count = 0       #counter for the numbers line in our file (numbers of links)
			for line in fhand:
				count = count + 1  #count the number links in our file

			counterRandom = randint(2, count) #Generate number between 2 until numbers of links
			count = 0

			fhand = open('ourlist.txt','r') #open file again

			for link in fhand: #take random link from our file
				count = count + 1
				if count == counterRandom:
					break

			while True:
				try: 
					yourTime = float(input('Set Your Time to play vedio (minutes): ')) #set time to delay playing vedio
					yourTime = yourTime * 60 #put time in minutes
					time.sleep(yourTime) #delay playing vedio
					webbrowser.open(link) #open link in browser
					break
				except Exception as e:
					print('This is not a time,Try again ') #printed when enter not time ass 'asd' or '456sad'
			
		except Exception as e:
			print('Sorry,Can not open file !!') #when app can not open the file

	def ourListLinks(self): #method that produce the link you choice from our list
		fhand = open('ourlist.txt','r')
		count = 0
		print('\n\n\t\t\t\t\tOur List \n\n')
		for line in fhand:
			count = count + 1
			print(count , " . ", line)

		numberchoice = int(input('Enter Your Choice : '))
		fhand = open('ourlist.txt','r')
		counts = 0
		for link in fhand:
			counts = counts + 1
			if counts == numberchoice:
				break
		yourTime = float(input('Set Your Time to play vedio (minutes) : ')) 
		yourTime = yourTime * 60
		time.sleep(yourTime)
		webbrowser.open(link)

	def specificLink(self): #method that open link you enter and you can add it to our list
		try:
			link = input('Enter Your Link : ') #take link from user
			add = input("Add this link to our list (y/n): ") #user can save his link in ourlist by press y

			if add == 'y': #when user enter y 
				fhand = open('ourlist.txt','a+') #open file to append new link
				fhand.write('\n') #write new line in our file
				fhand.write(link) #write the new link inour file
			elif add == 'n' : #if press n
				pass	
			else : 
				print('your choice is wrone,and the new link not saved') #when user pressed any key execpt y or no
			yourTime = float(input('Set Your Time to play vedio (minutes): ')) #set time by user
			yourTime = yourTime * 60 
			time.sleep(yourTime)
			webbrowser.open(link)
		except Exception as e:
			print("This is not a Time,Try again")
