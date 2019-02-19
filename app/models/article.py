class Article:
    '''
    Article class to define Article Objects
    '''

    def __init__(self,title,urlToImage,description,publishedAt,url):
        self.title = title
        self.urlToImage =urlToImage
        self.description = description
        self.publishedAt = publishedAt
        self.url = url
 