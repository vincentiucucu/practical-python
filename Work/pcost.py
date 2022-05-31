# pcost.py
#
# Exercise 1.33
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
        next(rows)
        for row in rows:
            try:
                total_cost += int(row[1]) * float(row[2])
            except ValueError as e:
                print(f'Warning: bad line; {e}')
        return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Work/Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total cost: {cost:.2f}')