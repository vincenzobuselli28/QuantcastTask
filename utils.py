from datetime import datetime

# Parses through a .csv file in the specified filepath
# and returns a 2d-dictionary that contains the number of times a specific
# cookie was logged. The dictionary is indexable by date and cookie hash, 
# e.g dict[date][cookie_hash] => count

def parseCookieLog(filepath):
    cookie_log_stream = open(filepath, 'r')
    cookie_logs = cookie_log_stream.readlines()[1:]
    entries_by_date = dict()

    # Parse through lines in the specified file
    for line in cookie_logs:
        cookie_log_entry = line.replace('\n','').split(',')

        # Split and store the cookie, date and time for every line
        cookie = cookie_log_entry[0]
        date, time = cookie_log_entry[1].split('T')

        # Check if the date is already in the dictionary
        if date not in entries_by_date.keys():
            entries_by_date[date] = dict()
        
        # Check if the cookie is already in the dictionary
        if cookie not in entries_by_date[date].keys():
            entries_by_date[date][cookie] = 0

        # Increase the total activity count of the cookie for that date
        entries_by_date[date][cookie] += 1
        
    return entries_by_date

# Returns a list of the most active cookies at a given date from a specified entry log

def mostActiveCookies(filepath, date):
    cookie_log = parseCookieLog(filepath)

    # get the maximum activity count for the specified date
    all_cookies = cookie_log[date].keys()
    most_activations = max([cookie_log[date][cookie] for cookie in all_cookies])

    # return all the cookies that match the maximum activity
    most_active = [cookie for cookie in all_cookies if cookie_log[date][cookie] == most_activations]

    return most_active