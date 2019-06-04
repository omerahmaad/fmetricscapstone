# This code is written by Omer Ahmad
# These are the codes to extract data for the api
import tmdbsimple as tmdb
import pandas as pd
import requests



analytical_data = pd.read_csv("Analytical_Data.csv")
tmdb.API_KEY = 'b5b1a2e5b5fb2a50ab7cfd9d31b1a509'

def title_from_id(id):
    tmdb.API_KEY = 'b5b1a2e5b5fb2a50ab7cfd9d31b1a509'
    movie = tmdb.Movies(id)
    response = movie.info()
    return movie.title

def movie_search(title):
    tmdb.API_KEY = 'b5b1a2e5b5fb2a50ab7cfd9d31b1a509'
    search = tmdb.Search()
    response = search.movie(query=title)
    data = []
    for s in search.results:
        data.append(s['title'])
    data = pd.DataFrame(data,columns = ['Name'])
    data = data.to_dict('record')
    return data

class movie_data():
    def __init__(self, movie_name):
        self.name = movie_name
        
    def movie_name(self):
        return self.name
    
    def movie_id(self):
        search = tmdb.Search()
        response = search.movie(query=self.name)
        for s in search.results:
            id = s['id']
        return str(id)
    def poster_address(self):
        search = tmdb.Search()
        response = search.movie(query=self.name)
        for s in search.results:
            path = ("https://image.tmdb.org/t/p/original{}".format(s['poster_path']))
        
        return path
        
    def overview(self):
        search = tmdb.Search()
        response = search.movie(query=self.name)
        for s in search.results:
            overview = (s['overview'])
        
        return overview
    
    def popularity(self):
        search = tmdb.Search()
        response = search.movie(query=self.name)
        for s in search.results:
            pop = (s['popularity'])
        
        return round(pop,2)
    
    def release_date(self):
        search = tmdb.Search()
        response = search.movie(query=self.name)
        for s in search.results:
            date = (s['release_date'])
        
        return date
    
    def budget(self):
        id = self.movie_id()
        movie = tmdb.Movies(id)
        response = movie.info()
        budget = movie.budget
        return budget
    
    def cast(self):
        id = self.movie_id()
        movie = tmdb.Movies(id)
        response = movie.info()
        data = movie.credits()
        cast = data['cast']
        return cast
    def crew(self):
        id = self.movie_id()
        movie = tmdb.Movies(id)
        response = movie.info()
        data = movie.credits()
        crew = data['crew']
        return crew
    
    def backdrop(self):
        search = tmdb.Search()
        response = search.movie(query=self.name)
        for s in search.results:
            path = ("https://image.tmdb.org/t/p/original{}".format(s['backdrop_path']))
            return path
    def production_company(self):
        id = self.movie_id()
        movie = tmdb.Movies(id)
        response = movie.info()
        return response['production_companies']
    def genre(self):
        id = self.movie_id()
        movie = tmdb.Movies(id)
        response = movie.info()
        return response['genres']
    def homepage(self):
        id = self.movie_id()
        movie = tmdb.Movies(id)
        response = movie.info()
        return response['homepage']
def top_movies():
    tmdb.API_KEY = 'b5b1a2e5b5fb2a50ab7cfd9d31b1a509'
    response = requests.get('https://api.themoviedb.org/3/discover/movie?api_key=' + tmdb.API_KEY + '&primary_release_year=2019&sort_by=popularity.desc')
    highest_pop = response.json() # store parsed json response
    highest_pop_films = highest_pop['results']
    return highest_pop_films



def act_Revenue(movie_name):
    result = analytical_data[analytical_data['Movie'] == movie_name]
    result = result.to_dict('record')
    act_Revenue = 0
    for s in result:
        act_Revenue = s['Actual_Revenue']
    act_Revenue = "${:,}".format(act_Revenue)
    return act_Revenue
def pred_Revenue(movie_name):
    result = analytical_data[analytical_data['Movie'] == movie_name]
    result = result.to_dict('record')
    act_Revenue = 0
    for s in result:
        act_Revenue = s['Predicted_Revenue']
    act_Revenue = "${:,}".format(act_Revenue)
    return act_Revenue
    

def top_movies_posters():
    tmdb.API_KEY = 'b5b1a2e5b5fb2a50ab7cfd9d31b1a509'
    response = requests.get('https://api.themoviedb.org/3/discover/movie?api_key=' + tmdb.API_KEY + '&primary_release_year=2019&sort_by=popularity.desc')
    highest_pop = response.json() # store parsed json response
    highest_pop_films = highest_pop['results']
    data = pd.DataFrame(highest_pop_films)
    poster = data[['poster_path']]
    poster['poster_path'] = "https://image.tmdb.org/t/p/original"+ poster['poster_path']
    poster = poster.head(6)
    return poster

def top_movies_title():
    tmdb.API_KEY = 'b5b1a2e5b5fb2a50ab7cfd9d31b1a509'
    response = requests.get('https://api.themoviedb.org/3/discover/movie?api_key=' + tmdb.API_KEY + '&primary_release_year=2019&sort_by=popularity.desc')
    highest_pop = response.json() # store parsed json response
    highest_pop_films = highest_pop['results']
    data = pd.DataFrame(highest_pop_films)
    title = data[['original_title']]
    title = title.head(6)
    return title

def top_movies_pop():
    tmdb.API_KEY = 'b5b1a2e5b5fb2a50ab7cfd9d31b1a509'
    response = requests.get('https://api.themoviedb.org/3/discover/movie?api_key=' + tmdb.API_KEY + '&primary_release_year=2019&sort_by=popularity.desc')
    highest_pop = response.json() # store parsed json response
    highest_pop_films = highest_pop['results']
    data = pd.DataFrame(highest_pop_films)
    pop = data[['popularity']]
    pop = pop.head(6)
    return pop

def poster_path(id, name):
    tmdb.API_KEY = 'b5b1a2e5b5fb2a50ab7cfd9d31b1a509'
    search = tmdb.Search()
    response = search.movie(query=name)
    data = []
    for s in search.results:
        if (s['id'] == id):
            data.append(s['poster_path'])
    data = str(data)
    data = data[3:len(data)-2]
    return "https://image.tmdb.org/t/p/original/{}".format(data)

def popularity_num(id, name):
    tmdb.API_KEY = 'b5b1a2e5b5fb2a50ab7cfd9d31b1a509'
    search = tmdb.Search()
    response = search.movie(query=name)
    data = []
    for s in search.results:
        if (s['id'] == id):
            data.append(s['popularity'])
    return str(data)[1:len(data)-3]

def release_date(id, name):
    tmdb.API_KEY = 'b5b1a2e5b5fb2a50ab7cfd9d31b1a509'
    search = tmdb.Search()
    response = search.movie(query=name)
    data = []
    for s in search.results:
        if (s['id'] == id):
            data.append(s['release_date'])
    data = str(data)
    data = data[2:len(data)-2]
    return data