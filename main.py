import random
import datetime as dt
import smtplib
##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
import pandas as pd
df=pd.read_csv("birthdays.csv")
name=""
msg=""
email=""
date=dt.datetime.now()
month_t=date.month
date_t=date.day
for index,date_new in df.iterrows():
    if date_new[3]==month_t and date_new[4]==date_t:
        name=date_new[0]
        email=date_new[1]
        break
if name:
    ran=random.choice(["letter_2.txt","letter_3.txt"])
    with open(f"letter_templates/{ran}","r") as f:
        for line in f.readlines():

            for word in line.strip().split(" "):
                if word=="[NAME],":
                    msg+=str(name)+","
                else:
                    msg+=word+" "
            msg+="\n"




# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

with smtplib.SMTP("smtp.gmail.com") as conn:
    conn.starttls()
    conn.login(user="jambah1801@gmail.com",password="Aamir@1801")
    conn.sendmail(from_addr="jambah1801@gmail.com",to_addrs="aamir1801@gmail.com",msg=f"Subject:Birthdaywish\n\n{msg}")



