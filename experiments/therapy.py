from time import sleep
print('HELLO. WELCOME TO PYTHON THERAPIST INDUSTRIES LIMITED. WE WILL BE HAPPY TO SERVE YOU.')
xh = input('Would you like to render our 100%  efficient therapist services?(yes/no):')
if xh.lower() == ('yes'):
	print('Thank you.')
	xw = input('Please state your name:  ')
	xe = input('Please state your gender(male/female): ')
	if xe.lower() == ('male'):
		xc = ('sir')
	elif xe.lower() == ('female'):
		xc = 'madam'
	input('so how are you feeling? ')

	input('I see. And why is that? ')

	input('Please elaborate. ')

	print(' wait for a second .')
	sleep(2)
	xd = input('are you, right now, feeling happy? ')
	if xd.lower() == ('yes'): 
		print('if, you are still feeling happy in 24 hrs, this session has been successful. if not, see you tomorrow. bye for now',xc)
		print(xw)
		quit()
	elif xd.lower() == ('no'):
		x = 2346
		print('I recommend you take some prozac')
		print('If this is not successful, please visit next monday at 10:12 AM')
		print('you can avail a special second visit discount of 40%. your 3 digit number will be shown in 10 seconds .')
		sleep(10)
		while x > 341:
			print(x)
			x = x - 1
		print('And your lucky code number for the special second visit discount is ... 342')
		print('Please show this code to the cashier on your next visit to avail a discount')
		print('thank you. ')
		print(' i hope you have enjoyed this session')
		print('bye',xw) 
		quit()
else:
	print('Okay, then. Bye!')








