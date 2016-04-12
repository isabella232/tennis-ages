#!/usr/bin/env python
from dateutil.parser import parse
from datetime import date

def process():
    today = date.today()

    with open('USA_-_womens_national_rankings.txt') as f:
        content = f.readlines()

    for line in content:
        line = line.strip()
        try:
            if line != '16 March 2016':
                born = parse(line)
                if born.year > 1940 and born.year < 2005:
                    age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
                    print '%s,%s' % (born, age)
        except ValueError:
            pass

if __name__ == '__main__':
    process()
