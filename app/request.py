from app import app
import urllib.request,json
from .models import source
from .models import article


Source = source.Source
Article = article.Article
# Getting api key
api_key = app.config['SOURCE_API_KEY']

# Getting the source base url
base_url = app.config["SOURCE_API_BASE_URL"]
base_url_articles = app.config["ARTICLE_API_BASE_URL"]


def get_sources(category):
    # print(get_sources)
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(category,api_key)
    # print(get_sources_url)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)
       

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)
    return source_results
           


def process_results(source_list):
    '''
    Function  that processes the source result and transform them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain source details

    Returns :
        source_results: A list of source objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        category = source_item.get('category')
        if name:
            source_object = Source(id,name,description,category)
            source_results.append(source_object)


    return source_results


def get_articles(id):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = base_url_articles.format(id, api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_response = json.loads(url.read())
        print( get_articles_response)
        article_results = None

        if get_articles_response['articles']:
            article_results_list = get_articles_response['articles']
            article_results = process_products(article_results_list)
    return article_results

def process_products(article_list):
    '''
    Function  that processes the article result and transform them to a list of Objects

    Args:
        article_list: A list of dictionaries that contain article details

    Returns :
        article_results: A list of article objects
    '''
    article_results =[]
    for article_item in article_list:
        title = article_item.get('title')
        urlToImage = article_item.get('urlToImage')
        description = article_item.get('description')
        publishedAt = article_item.get('publishedAt')
        url = article_item.get('url')
       
        if urlToImage:
            article_object = Article(title,urlToImage,description,publishedAt,url)
            article_results.append(article_object)   


    return article_results



