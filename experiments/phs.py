print('HELLO. WELCOME TO PYTHON THERAPIST INDUSTRIES LIMITED. WE WILL BE HAPPY TO SERVE YOU')
xh = input('Would you like to render our 100%  efficient therapist services?(yes/no)')
if xh == ('yes'):
	print('Thank you.')
	print('Please note that no capital letters are entertained in this session')
	xw = input('Please state your name  ')
	xe = input('Please state your gender ')
	if xe == ('male'):
		xc = ('sir')
	elif xe == ('female'):
		xc = 'madam'
	input('so how are you feeling')

	input('I see. And why is that?')

	input('And when did happen')

	print('Please wait for a second .')
	xd = input('are you, right now, feeling happy?')
	if xd == ('yes'):
		print('if, you are still feeling happy in 24 hrs, this session has been successful. if not, see you tomorrow. bye for now',xc)
		print(xw)
		quit()
	elif xd == ('no'):
		x = 2346
		print(' I recommend the drug prozac in a quantity of 15.78 grams three times a week ')
		print('If this is not successful, please visit next monday at 10:12 AM')
		print('you can avail a special second visit discount of 40%. your 3 digit number will be shown in 7 seconds .')
		b = 7
		sleep(b)
		while x > 341:
			print(x)
			x = x - 1
		print('And your lucky code number for the special second visit discount is ... 342')
		print('Please show this code to the cashier on your next visit to avail a discount')
		print('thank you. ')
		print(' i hope you have enjoyed this session')
		print('bye') 
		print(xw)
		quit()
elif xh == ('no'):
	print('bye')
	exit()








