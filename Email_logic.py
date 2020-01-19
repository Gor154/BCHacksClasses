from bs4 import BeautifulSoup
import requests
import email
import imaplib
import ast
import json
import smtplib

future_array = ["CHEM","123","001"]

link = "https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-section&dept=" + future_array[0]+"&course="+future_array[1]+"&section="+future_array[2]+"&campuscd=UBCO"
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



# email = 'classnotifier123@gmail.com'
# passwd = 'ritikaeatingfalafel' 
# #while(1==1):
#     with smtplib.SMTP('smtp.gmail.com',587) as smtp:
#         smtp.ehlo()
#         smtp.starttls()
#         smtp.ehlo()

#         smtp.login(email,passwd)

#         subject = 'This program will notify your chosen class'
#         body = 'Here is the information'

#         msg = f'Subject: {subject}\n\n{body}'

#         smtp.sendmail(email,'ilyeref@gmail.com',msg)