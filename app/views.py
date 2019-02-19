from flask import render_template
from app import app
from .request import get_sources, get_articles
# from .request import get_articles
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


@app.route('/article/<id>')
def article(id):
  '''
  View root page function that returns the index page and its data
  '''
  articles = get_articles(id)
  print(articles)
  return render_template('article.html', articles =  articles)