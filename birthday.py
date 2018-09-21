"""
birthday.py
Author: Ella Edmonds
Credit: None
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""
name = input ('Hello, what is your name? ')
a = input (str('Hi '+name+', what was the name of the month you were born? '))
b = float (input ('And what year were you born in, '+name+'? '))
c = float (input ('And the day? '))

if a is 'October' and c == 31:
    print('You were born on Halloween!')
elif a is 'September' and c == 19:
    print('Happy Birthday!')

else:
    if a in ['September','October','November']:
        season ='fall'
    elif a in ['December','January','February']:
        season = 'winter'
    elif a in ['March','April','May']:
        season = 'spring'
    elif a in ['June','July','August']:
        season = 'summer'
        
    if 0<=b<=1979:
        age = 'Stone Age.'
    elif 1980<=b<=1989:
        age = 'eighties.'
    elif 1990<=b<=1999:
        age = 'nineties.'
    elif 2000<=b<=2020:
        age = 'two thousands.'
        
    print(name+', you are a '+season+' baby of the '+age)
