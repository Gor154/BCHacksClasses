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
import seatMessenger

connection = mysql.connector.connect(host='34.82.183.200', database='Hackathon', user='id12288837_root', password='435566')


us = 'classnotifier123@gmail.com'
passw = 'ritikaeatingfalafel'

while (True):
    try:
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
        
        #print(message[0])
        title = message[0].split()
        course = title[0]
        number = title[1]
        section = title[2]
        email2 = title[3]

        print("Course: ", course)
        print("Number: ", number)
        print("Section: ", section)
        print("Email: ", email2)

        email_split = email2.split("@")
        # for i in email_split:
        #     print(i)

        if(course == "DELETE"):
            sql_del_query = "DELETE FROM Mailing_list WHERE email_1=\'"+email_split[0]+"\' AND email_2 = \'"+email_split[1]+"\';"
            cursor2 = connection.cursor()
            result1 = cursor2.execute(sql_del_query)
            connection.commit()
            continue
        

        sql_query = "INSERT INTO Mailing_list (Subject, Course_num, Section, email_1, email_2) VALUES(\'"+course+"\', \'"+number+"\', \'"+section+"\', \'"+email_split[0]+"\', \'"+email_split[1]+"\');"


        cursor1 = connection.cursor()
        result = cursor1.execute(sql_query)
        connection.commit()
        typ, data = mail.search(None, 'ALL')
        for num in data[0].split():
            mail.store(num, '+FLAGS', '\\Deleted')
        mail.expunge()





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




        email1 = 'classnotifier123@gmail.com'
        passwd = 'ritikaeatingfalafel' 

        #while(1==1):
        with smtplib.SMTP('smtp.gmail.com',587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            smtp.login(email1,passwd)

            subject = 'This program will notify your chosen class'
            body = course+" "+number+", section "+section+" has "+seats+" seats left"

            msg = f'Subject: {subject}\n\n{body}'

            smtp.sendmail(email1,email_split[0]+"@"+email_split[1],msg)
    except:
        time.sleep(15)