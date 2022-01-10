##################### Extra Hard Starting Project ######################
import csv

import pandas
import datetime as dt
import random
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
df=pandas.read_csv("birthdays.csv")
r=csv.reader(df)

dict={(data_row.day,data_row.month):data_row for (index,data_row) in df.iterrows()}
print(dict)
# print(r)
# for i in df.iterrows():
#     print(i)
#
#
#
# now=dt.datetime.now()
# day=now.day
# month=now.month
# NAME=""
# if(day==13 and month==1):
#     NAME="Shubham"
# elif(day==6 and month==1):
#     NAME="Ganesh"
#
#
# n=random.randint(1,3)
# f1=open(f"letter_templates/letter_{n}.txt","r")
# l1=f1.read()
# l1=l1.replace("[NAME]",NAME)
# print(l1)
# 4. Send the letter generated in step 3 to that person's email address.




