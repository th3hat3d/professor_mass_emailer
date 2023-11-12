#!/usr/bin/python3
import re
import requests
import smtplib

link = input("College staff link to be scraped: ")
page = requests.get(link).text
email_pattern = re.compile(r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4})')
email_matches = re.findall(email_pattern, page)
noduplicates = list(dict.fromkeys(email_matches))
for dest in noduplicates:
 s = smtplib.SMTP('smtp.gmail.com', 587)
 s.starttls()
 s.login("", "")
 message = open("email.txt").read()
 s.sendmail("", dest, message)
 s.quit()
