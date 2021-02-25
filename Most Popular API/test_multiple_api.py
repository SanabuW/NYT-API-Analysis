# Dependencies
from bs4 import BeautifulSoup
import requests
import pymongo

import json

# Initialize PyMongo to work with MongoDBs
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# Define database and collection
db = client.views_db
collection = db.articles2

# URL of page to be scraped
mostviewed_api = 'https://api.nytimes.com/svc/mostpopular/v2/viewed/30.json?api-key=UO0KtPw9TJHhMgofDtUHBKCzivb20tkN'
mostemailed_api = 'https://api.nytimes.com/svc/mostpopular/v2/emailed/30.json?api-key=UO0KtPw9TJHhMgofDtUHBKCzivb20tkN'
mostshared_api = 'https://api.nytimes.com/svc/mostpopular/v2/shared/30/facebook.json?api-key=UO0KtPw9TJHhMgofDtUHBKCzivb20tkN'

api_list = ['mostviewed_api', 'mostemailed_api', 'mostshared_api']

def get_api(api):
    response = requests.get(api)

    result = json.loads(response.content)

    most_popular_articles = result['results']
    most_popular_articles = [{'api': 'most_viewed' ,'title': x['title'], 'published_date': x['published_date'], 'adx_keywords': x['adx_keywords'].split(';')} for x in results]

   return most_popular_articles


dict_api = {}
for api in api_list:
    dict_api[api] = get_api(api)

document_list = []

documentlist.append(most_popular_articles())


collection.insert_many(document_list)