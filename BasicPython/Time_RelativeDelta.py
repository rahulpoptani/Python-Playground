from datetime import datetime, timedelta
from dateutil import relativedelta

def start_of_month(func_datetime: datetime = datetime.now()) -> datetime:
    return datetime.strptime(datetime.strftime(func_datetime, '%Y%m'), '%Y%m')

def end_of_month(func_datetime: datetime = datetime.now()) -> datetime:
    return start_of_month(func_datetime + relativedelta.relativedelta(months=1)) - relativedelta.relativedelta(minutes=1)

print(start_of_month())
print(end_of_month())