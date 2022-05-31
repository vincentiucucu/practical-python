# pcost.py
#
# Exercise 1.30
'''with open('Work/Data/portfolio.csv', 'rt') as portfolio:
    total_cost = 0
    next(portfolio)
    for line in portfolio:
        entry = line.split(',')
        total_cost += int(entry[1]) * float(entry[2])
    print(f'Total cost {total_cost:.2f}')'''

def portfolio_cost(filename):
    'Calculates the total cost of a portfolio'
    with open(filename, 'rt') as portfolio:
        total_cost = 0
        next(portfolio)
        for line in portfolio:
            entry = line.split(',')
            total_cost += int(entry[1]) * float(entry[2])
        return total_cost

cost = portfolio_cost('Work/Data/portfolio.csv')
print(f'Total cost: {cost:.2f}')