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

def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))
    for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10s} {price:>10s} {change:>10.2f}') 

def portfolio_report(portfolio_filename, prices_filename):
    portfolio = read_portfolio(portfolio_filename)
    current_prices = read_prices(prices_filename)
    report = make_report(portfolio, current_prices)
    return print_report(report)

portfolio_report('Work/Data/portfolio.csv', 'Work/Data/prices.csv')


