# birthday_paradox.py
#   This program explores the suprising probabilities of the "Birthday Paradox"
# by: Scott Gordon

import datetime, random

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
        for b, bday_b in enumerate(birthdays[a + 1 :]):
            if bday_a == bday_b:
                return bday_a


print("***** Welcome to The Birtday Paradox *****")

print('''The birthday paradox shows us that in a group of N people, the odds
that two of them have matching birthdays is suprisingly large.
This program uses a Monte Carlo simulation (repeated random simulation)
to explore this concept''')

MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True:
    print('How many birthdays shall I generate? (Max 100)')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        num_bdays = int(response)
        break
print()

