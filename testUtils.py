import random
from datetime import datetime
import string

# General utilities for automated and manual testing

# Prints the dictionary containing the activity of the cookies for each day
def printCookieLog(cookie_log):
    for day in cookie_log.keys():
        print(day)
        for cookie in cookie_log[day].keys():
            print('\t' + cookie + ': ' + str(cookie_log[day][cookie]))

# Generates a random date and time between 1969-12-31 and 2023-11-14
def randomDateTime():
    time = random.randint(0,1700000000)
    date = datetime.fromtimestamp(time)
    str_date = date.strftime("%Y-%m-%dT%H:%M:%S+00:00")
    return str_date

# Generates a random alphabetic string of 16 characters
def randomCookieHash():
    hash = ''.join(random.choice(string.ascii_letters) for i in range(16))
    return hash

# Writes a list of cookie entries to a specified location
def testLogToFile(logs, filename):
    with open('testlogs/' + filename, 'w') as file:
        file.write('cookie,timestamp\n')
        for log in logs:
            file.write(log[0]+','+log[1]+'\n')

# Various functions to generate lists of cookie entries
class generateEntries:
    # Generates random entries
    def random(rows):
        dates = [randomDateTime() for _ in range(rows)]
        hashes = [randomCookieHash() for _ in range(rows)]
        dates.sort(reverse=True)

        log = [list(entry) for entry in zip(hashes,dates)]

        return log

    # Generates entries with the same date and different cookies
    def sameDay(rows):
        date = randomDateTime()
        dates = [date for _ in range(rows)]
        hashes = [randomCookieHash() for _ in range(rows)]
        dates.sort(reverse=True)

        log = [list(entry) for entry in zip(hashes,dates)]
        return log

    # Generates entries with the same cookie and different dates
    def sameCookie(rows):
        hash = randomCookieHash()
        dates = [randomDateTime() for _ in range(rows)]
        hashes = [hash for _ in range(rows)]
        dates.sort(reverse=True)

        log = [list(entry) for entry in zip(hashes,dates)]
        return log