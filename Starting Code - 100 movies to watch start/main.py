import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(url=URL)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
raw_movies = soup.find_all(name="h3", class_="title")
movies = [movie.getText() for movie in raw_movies]
# movies.reverse()
movies = movies[::-1]
with open("movies.txt", "w", encoding="utf8") as file:
    for movie in movies:
        file.write(f"{movie}\n")



