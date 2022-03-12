# Name: Xu Wang
# unikey: xwan7005

import sys

#movie list
mv_ls = [
		"The Shining. 1980. 2h 26m. 10:00. Room 1",
		"Your Name. 2016. 1h 52m. 13:00. Room 1",
		"Fate/Stay Night: Heaven's Feel - III. Spring Song. 2020. 2h 0m. 15:00. Room 1",
		"The Night Is Short, Walk on Girl. 2017. 1h 32m. 17:30. Room 1",
		"The Truman Show. 1998. 1h 47m. 19:30. Room 1",
		"Genocidal Organ. 2017. 1hr 55m. 21:45. Room 1",
		"Jacob's Ladder. 1990. 1h 56m. 10:00. Room 2",
		"Parasite. 2019. 2h 12m. 12:15. Room 2",
		"The Dark Knight. 2008. 2h 32min. 14:45. Room 2",
		"Blade Runner 2049. 2017. 2h 44m. 17:45. Room 2",
		"The Mist. 2007. 2h 6m. 21:00. Room 2",
		"Demon Slayer: Mugen Train. 2020. 1h59min. 23:20. Room 2",
		"The Matrix. 1999. 2h 16m. 10:00. Room 3",
		"Inception. 2010. 2h 42m. 11:30. Room 3",
		"Shutter Island. 2010. 2h 19m. 14:30. Room 3",
		"Soul. 2020. 1hr 40m. 17:00. Room 3",
		"Mrs. Brown. 1997. 1h 41min. 19:00. Room 3",
		"Peppa Pig: Festival of Fun. 2019. 1h 8min. 21:00. Room 3",
		"Titanic. 1997. 3h 30min. 22:15. Room 3"
		]
#movie name list, upper-cased for case insensitive fuctions
mv_name = [
		"THE SHINING","YOUR NAME","FATE/STAY NIGHT: HEAVEN'S FEEL - III. SPRING SONG",
		"THE NIGHT IS SHORT, WALK ON GIRL","THE TRUMAN SHOW","GENOCIDAL ORGAN",
		"JACOB'S LADDER","PARASITE","THE DARK KNIGHT",
		"BLADE RUNNER 2049","THE MIST","DEMON SLAYER: MUGEN TRAIN",
		"THE MATRIX","INCEPTION","SHUTTER ISLAND",
		"SOUL","MRS. BROWN","PEPPA PIG: FESTIVAL OF FUN","TITANIC"
		]
#movie time list
mv_time = [
		'10:00','13:00','15:00',
		'17:30','19:30','21:45',
		'10:00','12:15','14:45',
		'17:45','21:00','23:20',
		'10:00','11:30','14:30',
		'17:00','19:00','21:00',
		'22:15'
		]
#movie room list
mv_rm = [
		'Room 1','Room 1','Room 1','Room 1','Room 1','Room 1',
		'Room 2','Room 2','Room 2','Room 2','Room 2','Room 2',
		'Room 3','Room 3','Room 3','Room 3','Room 3','Room 3','Room 3'
		]
#AUD currency list
currency_in_cents = [10000,5000,2000,1000,500,200,100,50,20,10,5]

#room seats 
room1_seats = 35
room2_seats = 136
room3_seats = 42

#list to put results in
ls_popcorn = []
ls_popcorn_price = []
ls_ppl = []

#welcome msg
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('~ Welcome to Pizzaz cinema ~')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

#first command
if len(sys.argv) < 2:
	print("Usage: python3 pizzaz.py [--show <timenow> | --book | --group]")
	exit()
switch = sys.argv[1]

#check room capacity
def check_rm_cap(mv_room):
	if mv_room == 'Room 1':
		rm_cap = round(room1_seats/2)
		return rm_cap
	elif mv_room == 'Room 2':
		rm_cap = int(room2_seats/2)
		return rm_cap
	elif mv_room == 'Room 3':
		rm_cap = int(room3_seats/2)
		return rm_cap
	pass

#function to convert time to minute
def time_to_min(tm):
	h,m = map(int,tm.split(':'))
	if h >= 24:
		return
	elif h < 0:
		return
	elif m >= 60:
		return
	elif m < 0:
		return
	elif len(tm)<5:
		return
	else:
		result = h*60 + m
	return result
	pass

#main switch, will be called at the end of program
def check_switch():
	if switch == '--show':
		if len(sys.argv)<3:
			print()
			print('Sorry. This program does not recognise the switch options.')
			print()
			print('Bye.')
			return
		else:
			try:
				tm = sys.argv[2]
				check_mvtm(tm)
			except:
				print()
				print('Sorry. This program does not recognise the time format entered.')
				print()
				print('Bye.')
				return
	elif switch =='--book' and len(sys.argv) == 2:
		check_book()
	elif switch =='--group' and len(sys.argv) == 2:
		check_group()
	else:
		print()
		print('Sorry. This program does not recognise the switch options.')
		print()
		print('Bye.')
		return
	return
	pass

#fuction to compare time and print mv names, called when --show
def check_mvtm(tm):
	for i in range(0,len(mv_time)):
		if time_to_min(tm) < time_to_min(mv_time[i]):
			print(mv_ls[i])
	print()
	print('Bye.')
	return
	pass

#check input movie name against stored data
def check_mv_nm():
	ipt_mv_name = input('What is the name of the movie you want to watch? ')
	while len(ipt_mv_name) < 4:
		ipt_mv_name = input('What is the name of the movie you want to watch? ')
	next_step = ipt_mv_name.upper() in mv_name	
	if next_step:
		for i in range(0,len(mv_ls)):
			if ipt_mv_name.upper() in mv_ls[i].upper():
				movie_rm = mv_rm[i]
				movie_tm = mv_time[i]
				return [next_step, movie_rm, movie_tm]
	while not next_step:
		ask = input('Sorry, we could not find that movie. Enter Y to try again or N to quit. ')
		
		while ask.upper() not in ['Y','N']:
			ask = input('Sorry, we could not find that movie. Enter Y to try again or N to quit. ')
			
		if ask.upper() == 'N':
			print('Bye.')
			next_step = False
			return [next_step]
		else:
			ipt_mv_name = input('What is the name of the movie you want to watch? ')
			while len(ipt_mv_name) < 4:
				ipt_mv_name = input('What is the name of the movie you want to watch? ')
			next_step = ipt_mv_name.upper() in mv_name	
			for i in range(0,len(mv_ls)):
				if ipt_mv_name.upper() in mv_ls[i].upper():
					movie_rm = mv_rm[i]
					movie_tm = mv_time[i]
					return [next_step, movie_rm, movie_tm]
	return [next_step, movie_rm, movie_tm]
	pass

#check book, fuction will be called when switch is --book
def check_book():
	if switch =='--book':
		while True:
			check_result = check_mv_nm()
			print()
			if check_result[0] == True:
				check_time = time_to_min(check_result[2])
				num_ppl = 1
				check_popcorn(num_ppl)
				ls_ppl.append(1)
				print()
				print('The seat number for person 1 is #17')
				print()
				final_price = check_price(check_time,num_ppl)
				print()
				check_change(final_price)
				print()
				print('Bye.')
				return
			else:
				return
	return
	pass

#check_group function will be called if input is --group
def check_group():
	if switch =='--group':
		while True:
			check_result = check_mv_nm()
			print()
			if check_result[0] == True:
				check_cap = check_rm_cap(check_result[1])
				check_time = time_to_min(check_result[2])
				while True:
					try:
						num_ppl = int(input('How many persons will you like to book for? '))
						print()
					except ValueError:
						continue
					while num_ppl < 2:
						ask = input('Sorry, you must have at least two customers for a group booking. Enter Y to try again or N to quit. ')
						while ask.upper() not in ['Y','N']:
							ask = input('Sorry, you must have at least two customers for a group booking. Enter Y to try again or N to quit. ')
						if ask.upper() == 'N':
							print('Bye.')
							return
						else:
							break
					while num_ppl > check_cap:
						ask = input('Sorry, we do not have enough space to hold {}'.format(num_ppl)
								+ ' people in the theater room of {} seats.'.format(check_cap)
								+ ' Enter Y to try a different movie name or N to quit.')
						while ask.upper() not in ['Y','N']:
							ask = input('Sorry, we do not have enough space to hold {}'.format(num_ppl)
									+ ' people in the theater room of {} seats.'.format(check_cap)
									+ ' Enter Y to try a different movie name or N to quit.')
						if ask.upper() == 'N':
							print('Bye.')
							return
						if ask.upper() == 'Y':
							check_result = check_mv_nm()
							if check_result[0] == True:
								check_cap = check_rm_cap(check_result[1])
								check_time = time_to_min(check_result[2])
							break
					while num_ppl >= 2 and num_ppl < check_cap:
						check_popcorn(num_ppl)
						print()
						check_seat(num_ppl)
						print()
						final_price = check_price(check_time,num_ppl)
						print()
						check_change(final_price)
						print('Bye.')
						return
			else:
				return					
	return
	pass

#check popcorn
def check_popcorn(num_ppl):
	if switch == '--group':
		i = 1
		while i <= num_ppl:
			ask = input('For person {}, would you like to order popcorn? Y/N '.format(i))
			while ask.upper() not in ['Y','N']:
				ask = input ('For person {}, would you like to order popcorn? Y/N '.format(i))
			if ask.upper() == 'Y':
				pop_size = input('Person {} wants popcorn. What size Small, Medium or Large? (S/M/L) '.format(i)).upper()
				while pop_size.upper() not in ['S','M','L']:
					pop_size = input('Person {} wants popcorn. What size Small, Medium or Large? (S/M/L) '.format(i)).upper()
				ls_popcorn.append(pop_size.upper())
				if pop_size.upper() == 'S':
					ls_popcorn_price.append(3.5)
				elif pop_size.upper() == 'M':
					ls_popcorn_price.append(5.0)
				elif pop_size.upper() == 'L':
					ls_popcorn_price.append(7.0)
			elif ask.upper() == 'N':
				ls_popcorn.append('N')
			i+=1
		return
	elif switch == '--book':
		ask = input('Would you like to order popcorn? Y/N ')
		while ask.upper() not in ['Y','N']:
			ask = input('Would you like to order popcorn? Y/N ')
		if ask.upper() == 'Y':
			pop_size = input('You want popcorn. What size Small, Medium or Large? (S/M/L) ')
			while pop_size.upper() not in ['S','M','L']:
				pop_size = input('You want popcorn. What size Small, Medium or Large? (S/M/L) ')
			ls_popcorn.append(pop_size.upper())
			if pop_size.upper() == 'S':
				ls_popcorn_price.append(3.5)
			elif pop_size.upper() == 'M':
				ls_popcorn_price.append(5.0)
			elif pop_size.upper() == 'L':
				ls_popcorn_price.append(7.0)
			return
		elif ask.upper() == 'N':
			ls_popcorn.append('N')
		return 
	return
	pass

#check seat
def check_seat(num_ppl):
	i = 1
	while i <= num_ppl:
		s = 2 * i -1
		print('The seat number for person {} is #{}'.format(i,s))
		ls_ppl.append(i)
		i += 1
	return
	pass
	
#check movie + popcorn prices
def check_price(check_time,num_ppl):
	popcorn_s = 3.5
	popcorn_m = 5.0
	popcorn_l = 7
	total_pop = sum(ls_popcorn_price)
	total_pop_discount = 0.2 * total_pop
	if check_time < 960  :
		ticket_price = 13
		ticket_discount_price = 1.3*num_ppl
		total_pop_discount = 0.2 * total_pop
		initial_price = round((ticket_price*num_ppl + total_pop),2)
		final_price = initial_price - ticket_discount_price - total_pop_discount
		if num_ppl == 1:
			print('For {} person, the initial cost is'.format(num_ppl).ljust(34, ' ') 
			+ '$'
			+ '{:0.2f}'.format(initial_price).rjust(5, ' '))
		elif num_ppl > 1:
			print('For {} persons, the initial cost is'.format(num_ppl).ljust(35, ' ') 
			+ '$'
			+ '{:0.2f}'.format(initial_price).rjust(5, ' '))
		i = 1
		while i <= num_ppl:
			print(' Person {}: Ticket before 16:00'.format(i).ljust(34, ' ') 
			+ '$' 
			+ '{:0.2f}'.format(ticket_price).rjust(5, ' '))
			if ls_popcorn[i-1] =='S':
				print(' Person {}: Small popcorn'.format(i).ljust(34, ' ') 
				+ '$' 
				+ '{:0.2f}'.format(popcorn_s).rjust(5, ' '))
			elif ls_popcorn[i-1] =='M':
				print(' Person {}: Medium popcorn'.format(i).ljust(34, ' ') 
				+ '$' 
				+ '{:0.2f}'.format(popcorn_m).rjust(5, ' '))
			elif ls_popcorn[i-1] =='L':
				print(' Person {}: Large popcorn'.format(i).ljust(34, ' ') 
				+ '$' 
				+ '{:0.2f}'.format(popcorn_l).rjust(5, ' '))
			i += 1
		if initial_price <= 100:
			no_discount = 0
			print()
			print(' No discounts applied{}'.format('').ljust(34, ' ') 
			+ '$' 
			+ '{:0.2f}'.format(no_discount).rjust(5, ' '))
			print()
			print('The final price is {}'.format('').ljust(34, ' ') 
			+ '$' 
			+ '{:0.2f}'.format(initial_price).rjust(5, ' '))
			final_price = initial_price
			return final_price
		if initial_price > 100:
			print()
			print(' Discount applied tickets x{}'.format(num_ppl).ljust(34, ' ') 
			+ '-$' 
			+ '{:.2f}'.format(ticket_discount_price).rjust(5, ' '))
			print(' Discount applied popcorn x{}'.format(len(ls_popcorn_price)).ljust(33, ' ') 
			+ '-$' 
			+ '{:.2f}'.format(total_pop_discount).rjust(5, ' '))
			print()
			print('The final price is {}'.format('').ljust(34, ' ') 
			+ '$' 
			+ '{:0.2f}'.format(final_price).rjust(5, ' '))
			return final_price
	elif check_time >= 960 :
		ticket_price = 15
		ticket_discount_price = 1.5*num_ppl
		initial_price = round((ticket_price*num_ppl + total_pop),2)
		final_price = initial_price - ticket_discount_price - total_pop_discount
		if num_ppl == 1:
			print('For {} person, the initial cost is'.format(num_ppl).ljust(34, ' ') 
			+ '$'
			+ '{:0.2f}'.format(initial_price).rjust(5, ' '))
		elif num_ppl > 1:
			print('For {} persons, the initial cost is'.format(num_ppl).ljust(35, ' ') 
			+ '$'
			+ '{:0.2f}'.format(initial_price).rjust(5, ' '))
		i = 1
		while i <= num_ppl:
			print(' Person {}: Ticket from 16:00'.format(i).ljust(34, ' ') 
			+ '$' 
			+ '{:0.2f}'.format(ticket_price).rjust(5, ' '))
			if ls_popcorn[i-1] =='S':
				print(' Person {}: Small popcorn'.format(i).ljust(34, ' ') 
				+ '$'
				+ '{:0.2f}'.format(popcorn_s).rjust(5, ' '))
			elif ls_popcorn[i-1] =='M':
				print(' Person {}: Medium popcorn'.format(i).ljust(34, ' ') 
				+ '$' 
				+ '{:0.2f}'.format(popcorn_m).rjust(5, ' '))
			elif ls_popcorn[i-1] =='L':
				print(' Person {}: Large popcorn'.format(i).ljust(34, ' ') 
				+ '$' 
				+ '{:0.2f}'.format(popcorn_l).rjust(5, ' '))
			i += 1
		if initial_price <= 100:
			no_discount = 0
			print()
			print(' No discounts applied{}'.format('').ljust(34, ' ') 
			+ '$' 
			+ '{:0.2f}'.format(no_discount).rjust(5, ' '))
			print()
			print('The final price is {}'.format('').ljust(34, ' ') 
			+ '$' 
			+ '{:0.2f}'.format(initial_price).rjust(5, ' '))
			final_price = initial_price
			return final_price
		if initial_price > 100:
			print()
			print(' Discount applied tickets x{}'.format(num_ppl).ljust(34, ' ') 
			+ '-$' 
			+ '{:.2f}'.format(ticket_discount_price).rjust(5, ' '))
			print(' Discount applied popcorn x{}'.format(len(ls_popcorn_price)).ljust(33, ' ') 
			+ '-$' 
			+ '{:.2f}'.format(total_pop_discount).rjust(5, ' '))
			print()
			print('The final price is {}'.format('').ljust(34, ' ') 
			+ '$' 
			+ '{:0.2f}'.format(final_price).rjust(5, ' '))
			return final_price
	return
	pass

#transaction and change fuction, will be called last in the stream
def check_change(final_price):
	while True:
		try:
			amt_paid = float(input('Enter the amount paid: $'))
		except ValueError:
			continue
		while round(amt_paid,2) < round(final_price,2):
			print('The user is ${:0.2f} short. Ask the user to pay the correct amount.'.format(final_price-amt_paid))
			break
		while amt_paid > final_price and (amt_paid * 100) % 5 != 0:
			print('The input given is not divisible by 5c. Enter a valid payment.')
			break
		while amt_paid >= final_price and (amt_paid * 100) % 5 == 0:
			change = float(amt_paid-final_price)
			print('Change: ${:0.2f}'.format(change))
			i = 0
			while i <=len(currency_in_cents)-1:
				if change *100 / currency_in_cents[i] >= 1:
					num_currency = change *100 / currency_in_cents[i]
					change = round((change *100 % currency_in_cents[i])/100 , 2)  
					if currency_in_cents[i] >= 100:
						print(' $' + '{:0.0f}:'.format(currency_in_cents[i]/100).rjust(3, ' ') 
						+ '{:.0f}'.format(int(num_currency)).rjust(2, ' '))
					elif currency_in_cents[i] < 100:					
						print(' ' + '{:0.0f}c:'.format(currency_in_cents[i]).rjust(2, ' ') 
						+ '{:.0f}'.format(int(num_currency)).rjust(2, ' '))
					continue
				i+=1
			return
			
	return
	pass

#main switch, calls other fuctions depending on input --book, --group or --show time
check_switch()




