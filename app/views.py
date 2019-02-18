from flask import render_template
from app import app
from .request import get_sources

# Views

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    general_sources = get_sources('general')
    sports_source = get_sources('sports')
    technology_source = get_sources('technology')
    title = 'Home - Welcome to The best New-Highlight Website Online'
    return render_template('index.html', title = title, general = general_sources, sports = sports_source, technology = technology_source )
# @app.route('/source/<source_id>')
# def source(source_id):

#     '''
#     View source page function that returns the source details page and its data
#     '''
#     return render_template('source.html',id = source_id)




# @app.route('/')
# def index():

#     '''
#     View root page function that returns the index page and its data
#     '''

#     # Getting popular movie
#     popular_movies = get_movies('popular')
#     print(popular_movies)
#     title = 'Home - Welcome to The best Movie Review Website Online'
#     return render_template('index.html', title = title,popular = popular_movies)