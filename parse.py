from bs4 import BeautifulSoup
import requests

r = requests.get('https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-section&dept=DATA&course=301&section=001')
#print(r.text[5000:6000])

soup = BeautifulSoup(r.text, 'html.parser')

courseName = soup.find('title').text
seats = soup.find_all('table')

print(courseName)
print(seats)