import requests
from bs4 import BeautifulSoup
from inflection import titleize

def titles_generator(links):
    titles = []

    def post_formatter(url):
        if 'posts' in url:
            url = url.split('/')[-1]
            url = url.replace('-', ' ')
            url = titleize(url)
            titles.append(url)


    for link in links:
        post_formatter(link['href'])

    return titles

r = requests.get('http://www.dailysmarty.com/topics/python')
soup = BeautifulSoup(r.text,'html.parser')
links = soup.find_all('a')

titles = titles_generator(links)

for title in titles:
    print(title)

"""
Posts
Installing Anaconda Python Data Science Platform
Python Libraries To Import For Data Science Programs
Shortcut For Opening The Object Inspector In Python Spyder
Python Script For Replacing Missing Data In A Machine Learning Algorithm
Python Script For Pulling In The Same Column From An Array Of Arrays
How To Implement Fizzbuzz In Python
How To Think Like A Computer Scientist
Base Case Example For How To Test A Python Class
Installing And Working With Pipenv
Steps For Building A Flask Api Application With Python 3
Coding Practice
How To Generate A Random String In Python
Environment Configuration For Python Development With Anaconda Ide
Importance Of Data Management
Difference Between Independent And Dependent Variables In Machine Learning 
    8a847667 5d7b 44ea 82c6 197e55095631
How To Import Data And Segment I And D Variables
Preprocessing
Help Object Inspector In Spyder
Replacing Nan Cells In Python With The Mean Median And Mode
Deep Dive Into Flask Marshmallow
Missing Value Management
Setting Up Test Validation And Training Sets Of Data
Create Concatenate And Convert Numpy Arrays Then Export Pandas Data Frame As Csv
Normalization And Feature Scaling
Numpy Data Types
Numpy Upcasting
Numpy Copy Function
Numpy Nan As A Placeholder
Python Library Imports
Simple Linear Regression
Multiple Variable Regression
Polynomial Regression
"""