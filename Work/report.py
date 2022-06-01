# report.py
#
# Exercises 2.4, 2.5, 2.6
import csv
from pprint import pprint

def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        header = next(f)
        for row in rows:
            holding = {'name':row[0], 'shares':int(row[1]), 'price':float(row[2])}
            portfolio.append(holding)
    return portfolio

def read_prices(filename):
    prices = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            if row:
                prices[row[0]] = float(row[1])
    return prices

portfolio = read_portfolio('Work/Data/portfolio.csv')
pprint(portfolio)
