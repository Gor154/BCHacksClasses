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
import time
try:
    while True:
        connection = mysql.connector.connect(host='34.82.183.200', database='Hackathon', user='id12288837_root', password='435566')
        login_email = 'classnotifier123@gmail.com'
        passwd = 'ritikaeatingfalafel' 

        sql_query = "SELECT * FROM Mailing_list;"


        cursor1 = connection.cursor()
        cursor1.execute(sql_query)
        records = cursor1.fetchall()
        data = []

        for rows in records:
            data.append(rows)
        course = ""
        number = ""
        section = ""
        email1 = ""
        email2 = ""
        for i in range(0,len(data)-1):
            course = data[i][0]
            number = data[i][1]
            section = data[i][2]
            email1 = data[i][3]
            email2 = data[i][4]
        email = email1+"@"+email2

        link = "https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-section&dept=" + course+"&course="+number+"&section="+section+"&campuscd=UBCO"
        r = requests.get(link)


        soup = BeautifulSoup(r.text, 'html.parser')

        courseName = soup.find('title').text

        seats = soup.find('td', text='Total Seats Remaining:').find_next_sibling('td').text
        time.sleep(10)
        new_seats = soup.find('td', text='Total Seats Remaining:').find_next_sibling('td').text
        if int(seats) == 0 and int(new_seats) == 1:
            with smtplib.SMTP('smtp.gmail.com',587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.ehlo()

                smtp.login(login_email,passwd)

                subject = 'A seat opened up!'
                body = "There are now "+ new_seats+" seats available in "+course+" "+number+", section "+section

                msg = f'Subject: {subject}\n\n{body}'

                smtp.sendmail(login_email,email,msg)
except:
    time.sleep(120)