from bs4 import BeautifulSoup
import requests
import email
import imaplib
import ast
import json
import smtplib
import email
import imaplib
import mysql.connector

connection = mysql.connector.connect(host='localhost', database='Hackathon', user='root', password='')


us = 'classnotifier123@gmail.com'
passw = 'ritikaeatingfalafel'

mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(us,passw)
mail.select("inbox")

result , data = mail.uid('search', None, "ALL")

item_list = data[0].split()

recent = item_list[-1]
oldest = item_list[0]

result2, email_data = mail.uid('fetch', recent, '(RFC822)')
email_string = email_data[0][1].decode("utf-8")


email_message = email.message_from_string(email_string)

b = email.message_from_string(email_string)
message = []

if b.is_multipart():
    for payload in b.get_payload():
        message.append(payload.get_payload())
else:
    print(b.get_payload())
    

print(message[0])
title = message[0].split()
course = title[0]
number = title[1]
section = title[2]
email = title[3]

print("Course: ", course)
print("Number: ", number)
print("Section: ", section)
print("Email: ", email)

email_split = email.split("@")
for i in email_split:
    print(i)



sql_query = "INSERT INTO Mailing_list (Subject, Course_num, Section, email_1, email_2) VALUES(\'"+course+"\', \'"+number+"\', \'"+section+"\', \'"+email_split[0]+"\', \'"+email_split[1]+"\');"


cursor1 = connection.cursor()
result = cursor1.execute(sql_query)
connection.commit()




link = "https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-section&dept=" + course+"&course="+number+"&section="+section+"&campuscd=UBCO"
r = requests.get(link)


soup = BeautifulSoup(r.text, 'html.parser')

courseName = soup.find('title').text

seats = soup.find('td', text='Total Seats Remaining:').find_next_sibling('td').text

if int(seats)>0:
    print("\nSeats available")
else:
    print("\nNo seats")

print(courseName)
print(seats)




email = 'classnotifier123@gmail.com'
passwd = 'ritikaeatingfalafel' 

#while(1==1):
with smtplib.SMTP('smtp.gmail.com',587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(email,passwd)

    subject = 'This program will notify your chosen class'
    body = course+" "+number+", section "+section+" has "+seats+" seats left"

    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(email,email_split[0]+"@"+email_split[1],msg)