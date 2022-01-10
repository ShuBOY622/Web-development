import smtplib
import pandas
import random
import datetime as dt



now=dt.datetime.now()
print(now)
weekday=now.weekday()
if(weekday==0 or weekday==1 or weekday==2 or weekday==3 or weekday==4 or weekday==5 or weekday==6 ):
    f1=open("quotes.txt")
    l1=f1.readlines()

    msg=f"Subject: Monday Motivation \n\nTodays quote : \n{random.choice(l1)} \n This was Python automated mail by \n Shubham Kakde"
    username="shuboyisalive@gmail.com"
    pass1="Shuboy@123"
    receiver="divyadahake1303@gmail.com"
    connection=smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=username,password=pass1)
    connection.sendmail(from_addr=username,to_addrs=receiver,msg=msg)
    connection.close()
else:
    print("Today is not ",now.weekday())