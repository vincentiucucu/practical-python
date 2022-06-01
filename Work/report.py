# report.py
#
# Exercises 2.4, 2.5, 2.6
import csv
from multiprocessing.dummy import current_process
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

initial_value = 0
gainloss = 0
portfolio = read_portfolio('Work/Data/portfolio.csv')
current_prices = read_prices('Work/Data/prices.csv')
for i in portfolio:
    initial_value += i['shares'] * i['price']
    gainloss += i['shares'] * (current_prices[i['name']] - i['price'])
current_value = initial_value + gainloss
print(f'Initial value of portfolio: {initial_value:.2f}')
print(f'Current value of portfolio: {current_value:.2f}')
print(f'Gain/Loss: {gainloss:.2f}')

