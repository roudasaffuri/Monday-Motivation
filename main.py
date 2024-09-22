import smtplib
import datetime as dt
import random

my_email = "roudasaffuri@gmail.com"
password = "**** **** **** ****"


now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0 :
    with open("quotes.txt") as quote_file:
        # file.readlines() to get a list of all the lines
        # in this quote_file and save it into all_quotes
        all_quotes = quote_file.readlines()

        quote = random.choice(all_quotes)



    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="saffuri87@gmail.com",
                            msg=f"Subject:Monday Motivation\n\n{quote}"
                            )
