from flask import Flask,render_template, request
import pandas as pd
import tmdbsimple as tmdb
from functions import movie_data,top_movies, act_Revenue, pred_Revenue,top_movies_title, top_movies_posters, top_movies_pop, poster_path, popularity_num,release_date
import datetime
from api_key import api_key
from datetime import datetime
import requests

app = Flask(__name__)

def movie_search(title):
    tmdb.API_KEY = api_key
    search = tmdb.Search()
    response = search.movie(query=title)
    data = []
    for s in search.results:
        data.append((s['id'],s['original_title'], s['release_date'][0:4]))
    data = pd.DataFrame(data)
    data.rename(columns={0: "id", 1: 'title', 2:'year'}, inplace=True)
    data = data.to_dict('record')
    return data

@app.route("/")
def index():
    top = top_movies_posters()
    title = top_movies_title()
    pop = top_movies_pop()
    pos0 = top['poster_path'][0]
    title0 = title['original_title'][0]
    pop0 = pop['popularity'][0]

    pos1 = top['poster_path'][1]
    title1 = title['original_title'][1]
    pop1 = pop['popularity'][1]

    pos2 = top['poster_path'][2]
    title2 = title['original_title'][2]
    pop2 = pop['popularity'][2]

    pos3 = top['poster_path'][3]
    title3 = title['original_title'][3]
    pop3 = pop['popularity'][3]

    pos4 = top['poster_path'][4]
    title4 = title['original_title'][4]
    pop4 = pop['popularity'][4]

    pos5 = top['poster_path'][5]
    title5 = title['original_title'][5]
    pop5 = pop['popularity'][5]



    return render_template("home.html",
    pos0 = pos0,
    title0 = title0,
    pop0 = pop0,

    pos1 = pos1,
    title1 = title1,
    pop1 = pop1,

    pos2 = pos2,
    title2 = title2,
    pop2 = pop2,
    
    pos3 = pos3,
    title3 = title3,
    pop3 = pop3,

    pos4 = pos4,
    title4 = title4,
    pop4 = pop4,

    pos5 = pos5,
    title5 = title5,
    pop5 = pop5,
    )
@app.route('/about')
def about_us():
     return render_template("about_us.html")

@app.route('/Model')
def method():
     return render_template("method.html")



@app.route("/search_results/results/<string:id>")
def results(id):
    tmdb.API_KEY = api_key
    movie = tmdb.Movies(id)
    response = movie.info()
    movie = movie.title
    data = movie_data(movie)
    budget = data.budget()
    budget = "${:,}".format(budget)
    r_date = release_date(int(id),str(movie))
    r_date = datetime.strptime(r_date, '%Y-%m-%d')
    r_date = r_date.strftime("%B %d, %Y")
    r_date= str(r_date)
    pop = popularity_num(int(id),str(movie))
    poster = poster_path(int(id),str(movie))
    backdrop = data.backdrop()
    overview = data.overview()
    homepage = data.homepage()
    crew = data.crew()
    crew = pd.DataFrame(data.crew())
    cast = pd.DataFrame(data.cast())
    cast = cast.head(5)
    cast = cast[['name']]
    cast = cast.to_dict('record')
    director = crew[crew['job'] == 'Director']
    director = director[['name']]
    director = director.to_dict('records')
    writer = crew[crew['job'] == 'Writer']
    writer = writer[['name']]
    writer = writer.to_dict('records')
    act_Rev = act_Revenue(movie)
    pred_Rev = pred_Revenue(movie)
    return render_template("results.html", 
    movie = movie,

    Budget = budget, Popularity=pop,
    release_date = r_date,
    poster_add = poster,
    backdrop = backdrop,
    overview = overview,
    homepage = homepage,
    director = director,
    writer = writer,
    cast = cast,
    act_Rev = act_Rev,
    pred_Rev = pred_Rev )

@app.route("/search_results", methods = ['POST'])
def search_results():
    print("===form", request.form)
    movie = request.form['Movie']
    search = movie
    data = movie_search(search)
    return render_template("search_results.html", data = data) 


if __name__ == '__main__':
	app.run(host="127.0.0.1",port=8080,debug=True)
