import datetime

##Date format
b_day = datetime.date(2012,3,21)
print(b_day)

today=datetime.date.today()

birthDay = b_day.strftime("%A-%B %d-%Y")
print(birthDay)

age = today-b_day
print(age)

print(today.weekday())
print(today.isoweekday())

##Time format

t = datetime.time(9,30,45,100000)
print(t)

print(t.hour)
print(t.minute)
print(t.second)
print(t.microsecond)

today = datetime.datetime.today()
print(today)
print(today.weekday())
print(today.date())
print(today.time())

print(today)
t_delta = datetime.timedelta(hours=20)
print(today+t_delta)

print(today)
t_delta = datetime.timedelta(days=20)
print(today+t_delta)