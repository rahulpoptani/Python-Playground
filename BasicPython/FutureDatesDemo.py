import datetime
import calendar

balance = 5000
interest_rate = 13 * 0.01
monthly_payment = 500

today = datetime.date.today()

days_in_current_month = calendar.monthrange(today.year, today.month)[1] # returns tuple of (month, days)
days_till_month_end = days_in_current_month - today.day

# Payment should start from next month, so we calculate month end and add 1
start_date = today + datetime.timedelta(days=days_till_month_end+1)
end_date = start_date

while balance > 0:
    interest_charge = (interest_rate / 12) * balance
    balance += interest_charge
    balance -= monthly_payment
    
    balance = round(balance, 2)
    if balance < 0:
        balance = 0
    
    print(end_date, balance)
    
    days_in_current_month = calendar.monthrange(end_date.year, end_date.month)[1]
    end_date = end_date + datetime.timedelta(days=days_in_current_month)
