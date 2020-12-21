import json
import requests

from bs4 import BeautifulSoup

response = requests.get('https://www.udemy.com/')

popularCoursesList = []
coursesByName = []
studentsOnCourse = []

if response.status_code == 200:
    soup = BeautifulSoup(response.text, features='html5lib')
    popularCourses = soup.find_all('a', {'class':'udlite-heading-md category-card--category-card-title-link--3PqTy'})
    
    for item in popularCourses:
        popularCoursesList.append(item.text)

    trending = soup.find_all('a', {'class':'trending-topics--link--2qohI'})

    for item in trending:
        coursesByName.append(item.text)

    students = soup.find_all('div', {'class':'trending-topics--count--31-Lz'})

    for item in students:
        studentsOnCourse.append(item.text)
else:
    print('Error')

print('Most popular courses:\n')
for i in range(len(popularCoursesList)):
    print(popularCoursesList[i])


print('\nCourses and students:\n')

for i in range(len(coursesByName)):
    print(f'{coursesByName[i]} - {studentsOnCourse[i]}')