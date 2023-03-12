import requests
from bs4 import BeautifulSoup
import csv
import openpyxl

file = openpyxl.Workbook()
# print(file.sheetnames)
papurr = file.active
papurr.title = "Assignment on Web Scraping"

papurr.append(['Name', 'Rank', 'Year', 'Rating'])

response = requests.get('https://www.imdb.com/chart/top/')
response.raise_for_status()  # if the url is invalid, same reason for try/except

soup = BeautifulSoup(response.text, 'html.parser')
# print(soup)

movies = soup.find('tbody', class_="lister-list").find_all('tr')
# print(movies)

for movie in movies:
    name = movie.find("td", class_="titleColumn").a.text
    rank = movie.find("td", class_="titleColumn").get_text(strip=True).split('.')[0]
    year = movie.find("td", class_="titleColumn").span.text.strip('()')
    rating = movie.find("td", class_="ratingColumn imdbRating").strong.text
    # print(name,rank,year,rating)
    # break
    papurr.append([name, rank, year, rating])


file.save("AssignmentComplete1.xlsx")
