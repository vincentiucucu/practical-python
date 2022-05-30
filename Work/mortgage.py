# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0
extra_payment_start_month = int(input('Enter the index of the month from which the extra payment will begin:'))
extra_payment_end_month = int(input('Enter the index of the last month in which the extra payment will be made:'))
extra_payment = int(input('Enter the amount to be paid extra:'))

while principal > 0:
    months += 1

    if months < extra_payment_start_month or months > extra_payment_end_month:
        total_monthly_payment = payment
    else:
        total_monthly_payment = payment + extra_payment

    if  principal < total_monthly_payment:
        total_paid += principal
        principal = 0
    else:
        principal = principal * (1+rate/12) - total_monthly_payment
        total_paid += total_monthly_payment
    
    print(months, round(total_paid, 2), round(principal, 2))

print('Total paid:', total_paid)
print('Months', months)
