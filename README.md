
#1. Store data:

Movie data is stored in 6 parts:
    1) mv_ls: High level data list, example element: "The Shining. 1980. 2h 26m. 10:00. Room 1"
    2) mv_name: Upper case movie name list, example element: "THE SHINING"
    3) mv_time: Movie time list, example element: '10:00'
    4) mv_rm: Movie room list, example element: 'Room 1'
    5) currency_in_cents: AUD currency in cents. i.e: $100 is 10,000C in the list, $50 is 5,000C etc.
    6) room_seats: variables example: room1_seats = 35

#2. Error checking on time/comparison:

This program does time error checking/ comparison by converting HH:MM string format to number of minutes.
Fuction time_to_min(tm) does the converting job for the input time as well as the selected movie time.
Fuction check_mvtm(tm) does the checking/comparison job by comparing the converted times
Error checking factors in the following items: 
    1) length of input time <> 5 as len('HH:MM') = 5
    2) do not contain ':'
    3) input HH:MM where HH or MM is not an integer
    4) input HH:MM where HH in [00,24) and MM in [00,60)

#3. idioms 
order by orrurance:
    1) check_rm_cap(mv_room)    
       a small function converting Room numbers to seat capacities, called in check_group to check against number of people
    2) time_to_min(tm)
       a small function converting tm = (HH:MM) to number of minutes, called in check_mvtm(tm) to check input time against movie time
    3) check_switch()
       Main switch, called at the end. this is the main fuction that directs the program to other parts depending on switch input
    4) check_mvtm(tm)
       a small fuction to compare converted times, called in check_switch() when --show 
    6) check_mv_nm()
       a major fuction to check input movie name against stored data
       output a list [next_step, movie_rm, movie_tm]
       this function is essential to check_book() and check_group()
    7) check_book()
       fuction when --book is called in switch
    8) check_group()
       fuction when --group is called in switch
    9) check_popcorn(num_ppl)
       a downstream fuction in check_book and check_group to check popcorn orders
       output appends result data into list ls_popcorn = [] which will later be called in price calculation
    10) check_seat(num_ppl)
       a small fuction printing seat allocation
    11) check_price(check_time,num_ppl)
       a downstream fuction to calculate prices
    12) check_change(final_price)
       a downstream fuction to input transaction and calculate changes
