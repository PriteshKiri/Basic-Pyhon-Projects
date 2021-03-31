from PIL import Image
from random import randint


randomm =  randint(1,6)

im = Image.open('dice.jpg')

while True :

	inp = input("Please type 'ROLL' to roll the dice : ")
	
	if inp == 'ROLL':
		
		def roll(value):


			if value==1:
				box = (0,0,333,342)
				portion1 = im.crop(box)
				portion1.show()

			if value==2:
				box = (333,0,666,342)
				portion2 = im.crop(box)
				portion2.show()

			if value==3:
				box = (666,0,999,342)
				portion3 = im.crop(box)
				portion3.show()	

			if value==4:
				box = (0,342,333,685)
				portion4 = im.crop(box)
				portion4.show()
				 	
			if value==5:
				box = (333,342,666,685)
				portion5 = im.crop(box)
				portion5.show()	

			if value==6:
				box = (666,342,1000,680)
				portion6 = im.crop(box)
				portion6.show()	

		roll(randomm)
		break

	else:

		print(f"WRONG INPUT ! you have entered '{inp}'")

