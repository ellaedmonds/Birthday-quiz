"""
birthday.py
Author: <your name here>
Credit: <list sources used, if any>
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

if a is 'october' and c == 31:
    print('You were born on Halloween!')
if a is 'september' and c == 19:
    print('Happy Birthday!')

if a is 'september'or'october'or'november':
    season = 'fall'

if a is 'december'or'january'or'february':
    season = 'winter'
    
if a is 'march'or'april'or'may':
    season = 'spring'
    
if a is 'june'or'july'or'august':
    season = 'summer'
    
print(season)
