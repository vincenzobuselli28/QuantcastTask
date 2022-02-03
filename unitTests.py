from testUtils import *
import unittest
from unittest import TestCase

from utils import parseCookieLog, mostActiveCookies

class TestParseLog(TestCase):
    # Test that all the cookies in an input file are in the dictionary
    def test_log_contains_entries(self):
        entries = generateEntries.random(100)
        testLogToFile(entries, "test_log_contains_entries.csv")

        all_cookies = [entry[0] for entry in entries]
        log = parseCookieLog("testlogs/test_log_contains_entries.csv")

        cookies_in_log = []
        for date in log.keys():
            cookies_in_log += log[date].keys()

        assert(set(all_cookies) == set(cookies_in_log))

    # Test that all the dates in an input file are in the dictionary
    def test_log_dates_contains_cookies(self):
        entries = generateEntries.random(100)
        testLogToFile(entries, "test_log_dates_contain_cookies.csv")

        log = parseCookieLog("testlogs/test_log_dates_contain_cookies.csv")

        for entry in entries:
            assert(entry[0] in log[entry[1][:10]].keys())
    
    # Test that the input file is parsed correctly even if all the cookies are the same
    def test_one_cookie(self):
        entries = generateEntries.sameCookie(100)
        testLogToFile(entries, "test_only_one_cookie.csv")

        log = parseCookieLog("testlogs/test_only_one_cookie.csv")

        for date in log.keys():
            assert(len(log[date].keys()) == 1)

class TestMostActiveCookie(TestCase):
    # Test that the input file is parsed correctly even if all the cookies are the same
    def test_only_one_cookie(self):
        entries = generateEntries.sameCookie(100)
        testLogToFile(entries, "test_only_one_cookie.csv")

        date = entries[0][1][:10]

        mostActive = mostActiveCookies("testlogs/test_only_one_cookie.csv", date)

        assert(len(mostActive) == 1)
        assert(mostActive[0] == entries[0][0])

    # Test the given working example
    def test_manual(self):
        cookies = mostActiveCookies("testlogs/cookie_log.csv")
        assert(cookies == ["AtY0laUfhglK3lC7"])

if __name__ == '__main__':
    unittest.main()