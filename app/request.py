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
        # title = source_item.get('original_title')
        # overview = source_item.get('overview')
        # poster = source_item.get('poster_path')
        # vote_average = source_item.get('vote_average')
        # vote_count = source_item.get('vote_count')

        if name:
            source_object = Source(id,name,description,category)
            source_results.append(source_object)


    return source_results

def get_source(id):
    get_source_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_source_details_url) as url:
        source_details_data = url.read()
        source_details_response = json.loads(source_details_data)

        source_object = None
        if source_details_response:
            id = source_details_response.get('id')
            name = source_details_response.get('name')
            description = source_details_response.get('description')
            category = source_details_response.get('category')

            # title = source_details_response.get('original_title')
            # overview = source_details_response.get('overview')
            # poster = source_details_response.get('poster_path')
            # vote_average = source_details_response.get('vote_average')
            # vote_count = source_details_response.get('vote_count')

            source_object = Source(id,name,description,category)

    return source_object

def get_articles(category):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        article_results = None

        if get_articles_response['articles']:
            article_results_list = get_articles_response['articles']
            article_results = process_results(article_results_list)

def process_results(article_list):
    '''
    Function  that processes the article result and transform them to a list of Objects

    Args:
        article_list: A list of dictionaries that contain article details

    Returns :
        article_results: A list of article objects
    '''
    article_results = []
    for article_item in article_list:
        urlToImage = article_item.get('urlToImage')
        description = article_item.get('description')
        publishedAt = article_item.get('publishedAt')
        # poster = article_item.get('poster_path')
        # vote_average = article_item.get('vote_average')
        # vote_count = article_item.get('vote_count')

        if urlToImage:
            article_object = Article(urlToImage,description,publishedAt)
            article_results.append(article_object)   


    return article_results



