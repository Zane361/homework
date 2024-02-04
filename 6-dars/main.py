import classes

days = classes.Weekdays()
for day in days:
    print(day)

months = classes.Months()
for month in months:
    print(month)

user_1 = classes.Users('Ism_1', 'Familiya_1', 'Email_1')
user_2 = classes.Users('Ism_2', 'Familiya_2', 'Email_2')
user_3 = classes.Users('Ism_3', 'Familiya_3', 'Email_3')
user_4 = classes.Users('Ism_4', 'Familiya_4', 'Email_4')
user_5 = classes.Users('Ism_5', 'Familiya_5', 'Email_5')

for user in user_1:
    print(user)