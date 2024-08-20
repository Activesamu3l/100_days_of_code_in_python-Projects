import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
empire_webpage = response.text

soup = BeautifulSoup(empire_webpage, "html.parser")

titles = soup.find_all(name="h3", class_="title")

movie_title = [title.getText() for title in titles]
reversed_title = movie_title[::-1]
for title in reversed_title:
    print(title)
    with open("movies.text", "a") as file:
        file.writelines(f"{title}\n")
