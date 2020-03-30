import requests
import json
from config import OMDB_API_KEY

def getOMDBData(title):  # function queries OMDB api and returns JSON blurb

    movie_title = title

    url = 'http://www.omdbapi.com/'

    params = {
        'apikey': OMDB_API_KEY,
        't': movie_title,
        'r': 'json'
    }
    try:
        r = requests.get(url, params)

        data = json.loads(r.content)  # type = dict


        string = f""

        if data['Response'] == 'True':
            # To output pretty/formatted JSON
            out = json.dumps(data, indent=4)
            string += out

        else:
            string += f"False."

        if string == "False.":
            return False
        else:
            return print(string)

    except requests.ConnectionError:  # if no Internet connection, catch error
        return False

getOMDBData('Black Panther')

def getMoviesData(titles):  # get movie data when passed a list of movie titles

    movies = titles

    output = []

    for movie in movies:
        url = 'http://www.omdbapi.com/'

        params = {
            'apikey': OMDB_API_KEY,
            't': movie,
            'r': 'json'
        }

        r = requests.get(url, params)

        data = json.loads(r.content)  # type = dict
        output.append(data)

    return output


def getValidMoviesData(titles):  # process some validation to see if the movie titles exist

    movies = titles

    output = []

    call = getMoviesData(movies)

    for item in call:
        if item['Response'] == "True":
            output.append(item)

    return output

l = []

for d in getValidMoviesData(["Black Panther", "Clue", "foobarbat"]):
    l.append(d['Title'])
print(l)


def sortedMoviesData(titles):  # sort movie data based on IMDB Rating value

    movies = titles

    data = getValidMoviesData(movies)

    sortList = []
    output = []

    for item in data:
        sortList.append((item['Title'], item['imdbRating']))
    sortList = sorted(sortList, key=lambda x: x[1], reverse=True)
    for k, v in sortList:
        for item in data:
            if item['Title'] == k:
                output.append(item)

    return output

result = sortedMoviesData(["Superbabies: Baby Geniuses 2",
                  "The Shawshank Redemption",
                  "asdfasdfasdfasdfasdf" ,
                  "Source Code"])

l = []
for d in result:
   l.append(d['Title'])
print(l)

#
#  Exercises below deal with file handling
#

PREVIOUSLY_VIEWED_FNAME = 'viewed_movies.txt'

try:
    with open(PREVIOUSLY_VIEWED_FNAME, 'r') as file:
        viewed_movies = json.load(file)
except FileNotFoundError:  # if file does not exist, initialize variable to empty list
    viewed_movies = []

def markAsViewed(title):

    if title not in viewed_movies:
        viewed_movies.append(title)

        with open(PREVIOUSLY_VIEWED_FNAME, 'w') as output:
            json.dump(viewed_movies, output)



def hasSeenMovie(title):

    with open(PREVIOUSLY_VIEWED_FNAME, 'r') as file:

        seen = json.load(file)

        if title in seen:
            return True
        else:
            return False

print(hasSeenMovie('Iron Man 3'))
print(hasSeenMovie('fdgdhfghdfg'))
