# report.py
#
# Exercises 2.9, 2.10, 2.11, 2.12
import csv
from multiprocessing.dummy import current_process
from pprint import pprint

def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows)
        for rowno, row in enumerate(rows, start=1):
            holding = dict(zip(header, row))
            print(type(holding['price']))
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

def make_report(portfolio, prices):
    report = []
    for i in portfolio:
        change = prices[i['name']] - float(i['price'])
        current_price = '$' + str(prices[i['name']])
        record = (i['name'], i['shares'], current_price, change)
        report.append(record)
    return report

# get table info
portfolio = read_portfolio('Work/Data/portfoliodate.csv')
current_prices = read_prices('Work/Data/prices.csv')
report = make_report(portfolio, current_prices)
# print header and separating line
headers = ('Name', 'Shares', 'Price', 'Change')
print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
print('-' * 10, '-' * 10, '-' * 10, '-' * 10)
# print values
for name, shares, price, change in report:
    print(f'{name:>10s} {shares:>10s} {price:>10s} {change:>10.2f}')

'''
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
'''


