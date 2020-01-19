from bs4 import BeautifulSoup
import requests

r = requests.get('https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-section&dept=DATA&course=301&section=001&campuscd=UBCO')


soup = BeautifulSoup(r.text, 'html.parser')

courseName = soup.find('title').text

seats = soup.find('td', text='Total Seats Remaining:').find_next_sibling('td').text

if int(seats)>0:
    print("\nSeats available")
else:
    print("\nNo seats")

print(courseName)
print(seats)