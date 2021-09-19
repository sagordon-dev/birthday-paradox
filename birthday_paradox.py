# birthday_paradox.py
#   The birthday paradox shows us that in a group of N people, the odds
#   that two of them have matching birthdays is suprisingly large.
#   This program uses a Monte Carlo simulation (repeated random simulation)
#   to explore this concept.
# by: Scott Gordon

import datetime
import random


def get_birthdays(num_of_bdays):
    """Returns a list of number random date objects for birthdays."""
    birthdays = []
    for i in range(num_of_bdays):
        start_of_year = datetime.date(2001, 1, 1)

        ran_num_of_days = datetime.timedelta(random.randint(0, 364))
        bday = start_of_year + ran_num_of_days
        birthdays.append(bday)
    return birthdays


def get_match(birthdays):
    """Returns the date object of a birthday that occurs more than once
    in the birthdays list."""
    if len(birthdays) == len(set(birthdays)):
        return None

    for a, bday_a in enumerate(birthdays):
        for b, bday_b in enumerate(birthdays[a + 1:]):
            if bday_a == bday_b:
                return bday_a


print("***** Welcome to The Birtday Paradox *****\n")

MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True:
    print('How many birthdays shall I generate? (Max 100)')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        num_bdays = int(response)
        break
print()

print(f'Here are {num_bdays} birthdays:\n')
birthdays = get_birthdays(num_bdays)
for i, bday in enumerate(birthdays):
    if i != 0:
        print(', ', end='')
    month_name = MONTHS[bday.month - 1]
    date_text = f'{month_name} {bday.day}'
    print(date_text, end='')

match = get_match(birthdays)

print('In this simulation, ', end='')
if match != None:
    month_name = MONTHS[match.month - 1]
    date_text = f'{month_name} {match.day}'
    print('Multiple people have a birthday on', date_text)
else:
    print('there are no matching birthdays.')
print()

print(f'Generating {num_bdays} random birthdays 100,000 times...')
input('Press Enter to begin...')

print('Let\'s run another 100,000 simulations.')
sim_match = 0
for i in range(100000):
    if i % 10000 == 0:
        print(f'{i} simulations run...')
    birthdays = get_birthdays(num_bdays)
    if get_match(birthdays) != None:
        sim_match += 1
print('100,000 simulations run.')

probability = round(sim_match / 100000 * 100, 2)
print(f'Out of 100,000 simulations of {num_bdays} people, there was a')
print(f'matching birthday in that group {sim_match} times. This means')
print(f'that {num_bdays} people hava a {probability} % chance of')
print('having a matching birthday in their group.')
print('That\'s probably more than you would think!')
