import email
import imaplib

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
name = title[3]

print("Course: ", course)
print("Number: ", number)
print("Section: ", section)
print("Email: ", name)

