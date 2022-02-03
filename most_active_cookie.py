import argparse
from utils import mostActiveCookies

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', help='relative filepath to .csv log')
    parser.add_argument('-d', help='specified date')
    args = vars(parser.parse_args())

    cookies = mostActiveCookies(args['filepath'], args['d'])

    for cookie in cookies:
        print(cookie)
