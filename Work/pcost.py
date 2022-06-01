# pcost.py
#
# Exercise 2.16
'''with open('Work/Data/portfolio.csv', 'rt') as portfolio:
    total_cost = 0
    next(portfolio)
    for line in portfolio:
        entry = line.split(',')
        total_cost += int(entry[1]) * float(entry[2])
    print(f'Total cost {total_cost:.2f}')'''
import csv
import sys

def portfolio_cost(filename):
    'Calculates the total cost of a portfolio'
    with open(filename, 'rt') as portfolio:
        total_cost = 0
        rows = csv.reader(portfolio)
        header = next(rows)
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(header, row))
            try:
                total_cost += int(record['shares']) * float(record['price'])
            except ValueError as e:
                print(f'Row {rowno}: Couldn\'t convert {row} - {e}')
        return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Work/Data/portfoliodate.csv'

cost = portfolio_cost(filename)
print(f'Total cost: {cost:.2f}')