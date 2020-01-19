from bs4 import BeautifulSoup
import requests

r = requests.get("https://courses.students.ubc.ca/cs/courseschedule?tname=subj-section&course=121&section=101&campuscd=UBCO&dept=COSC&pname=subjarea")
#print(r.text[5000:6000])

soup = BeautifulSoup(r.text, 'html.parser')

courseName = soup.find('title').text
seats = soup.find_all('table')

print(courseName)
print(seats)