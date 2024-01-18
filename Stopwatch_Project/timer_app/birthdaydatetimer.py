import time
import datetime
from datetime import date

# def birthday_countdown(birthday):
#     today=datetime.date.today()
#     next_birthday=datetime.date(today.year+1,birthday.month,birthday.day)
#     if next_birthday < today:
#             next_birthday=datetime.date(today.year+1,birthday.month,birthday.day)

      
#     time_until_birthday = next_birthday - today
#     days_until_birthday = time_until_birthday.days

#     print("There are", days_until_birthday, "days until your birthday!")

# # Get the birthday from the user
# birthday_str = input("Enter your birthday (YYYY-MM-DD): ")
# birthday = datetime.datetime.strptime(birthday_str, "%Y-%m-%d").date()

# # Start the countdown
# birthday_countdown(birthday)

# import datetime

# def get_user_birthday():
#     year = int(input('When is your birthday? [YY] '))
#     month = int(input('When is your birthday? [MM] '))
#     day = int(input('When is your birthday? [DD] '))

#     birthday = datetime.datetime(year,month,day)
#     # print(birthday)
#     return birthday


# def calculate_dates(original_date, now):
#     date1 = now
#     date2 = datetime.datetime(now.year, original_date.month, original_date.day)
#     delta = date2 - date1
#     days = delta.total_seconds() / 60 /60 /24

#     return days


# def show_info(self):
#     pass



# bd = get_user_birthday()
# now = datetime.datetime.now()
# c = calculate_dates(bd,now)
# print(c)
def get_user_birthday():
    year = int(input('When is your birthday? [YY] '))
    month = int(input('When is your birthday? [MM] '))
    day = int(input('When is your birthday? [DD] '))

    birthday = datetime.datetime(year,month,day)
    return birthday


def calculate_dates(original_date, now):
    date1 = now
    date2 = datetime.datetime(now.year, original_date.month, original_date.day)
    delta = date2 - date1
    days = delta.total_seconds() / 60 /60 /24

    return days


def show_info(self):
    pass



bd = get_user_birthday()
now = datetime.datetime.now()
c = calculate_dates(bd,now)
print(c)


today = date.today()

def user_birthday():
    year = int(input('When is your birthday? [YY] '))
    month = int(input('When is your birthday? [MM] '))
    day = int(input('When is your birthday? [DD] '))

    birthday = datetime(year,month,day)
    return birthday

def calculate_dates(birthday):
    today == date.fromtimestamp(time.time())
    birthday = date(today.year, birthday.month, birthday.day)
    if birthday < today:
        birthday = birthday.replace(year=today.year + 1)
        return birthday
    else:
        return birthday
    
bday = user_birthday()
t = calculate_dates(bday)
time_to_birthday = abs(t-today)
days=str(time_to_birthday.days)
print("Time to Birthday is :" + days + " days")