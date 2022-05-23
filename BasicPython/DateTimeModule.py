import datetime

d = datetime.date(2021,9,1)
td = datetime.date.today()

print(d)
print(td)
print(td.year)
print(td.month)
print(td.day)
print(td.weekday()) # Monday 0 Sunday 6
print(td.isoweekday()) # Monday 1 Sunday 7


# addition substraction time and date

tdelta = datetime.timedelta(days = 7)

print(td + tdelta)

bday = datetime.date(2021, 10, 2)

till_bday = bday - td

print(till_bday.days)


t = datetime.time(9, 30, 30, 100000)

print(t)

# If you need date as well as time, then use datetime

dtdt = datetime.datetime(2021,9,1,9,30,30,100000)

print(dtdt)

print(dtdt.date()) # just get the date from datetime
print(dtdt.time()) # just get the time from datetime
print(dtdt.year) # just get the year from datetime


dt_today = datetime.datetime.today() # Returns current local datetime with timezone None
dt_now = datetime.datetime.now() # Gives option to pass timezone
dt_utcnow = datetime.datetime.utcnow()

print(dt_today) 
print(dt_now) 
print(dt_utcnow) # System time in UTC


##############################################################################################################################################
print('###################################')
import pytz

dt_now = datetime.datetime.now()
dt_now_utc = datetime.datetime.now(tz=pytz.UTC)

print(dt_now)
print(dt_now_utc)

# Convert from UTC to my timezone

dt_mine_tz = dt_now_utc.astimezone(pytz.timezone('Asia/Kolkata'))
print(dt_mine_tz)


# List all timezone

for tz in pytz.all_timezones:
    print(tz)