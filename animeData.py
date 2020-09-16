import requests
import json

import random

number = random.randrange(1,100)
print(number)

#note: format the string so you can use a random number
ANIME_URL = 'https://api.jikan.moe/v3/anime/{}/recommendations'
ANIME_URL=ANIME_URL.format(number)

print(ANIME_URL)

#generator
def get_recommended(re):
    for index in range(3):
        yield re['recommendations'][index]['title']

response = requests.get(ANIME_URL)
#print(response)
data = response.json()
anime_list = get_recommended(data)

for anime in anime_list:
    print(anime)


