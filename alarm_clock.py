#This is app that open vedio on youtube 
#1. random from saved list on it
#2. choice one vedio from our list 
#3. Put your link
# and after this you can put the time to the vedio play after it 
from clocks import OurObject #This import our class from our model that we created

print('\n\n\t\tAlarm Clock That play youtube vedio after some time\n')#sample description for program
print('1.Random vedio from Our List\t2.Our List\t3.Your vedio\n\n') # app features 
while True: #when you enter not a number you try and try to enter a number
	try: #when user enter not a number
		chocie = int(input('Enter Your chocie : ')) #take the user choice
		if chocie == 1 or chocie == 2 or chocie == 3 :
			break #break the loop when choice the number 1 or 2 or 3
		else :
			print('Sorry, This out of Rang !!') #printed when user enter a number out of app range
	except Exception as e:
		print('Not a number please Try Again') #print when user enter not a number


obj = OurObject() #decleare object from class OurObject()
if chocie == 1: 
	obj.randomLink() #calling randomLink() method when user choice number 1
elif chocie == 2 :
	obj.ourListLinks() #calling ourListLinks() method when user choice number 2
elif chocie == 3 :
	obj.specificLink() #calling specifcLink() method when user choice number 3




