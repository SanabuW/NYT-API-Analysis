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
url = 'https://api.nytimes.com/svc/mostpopular/v2/viewed/30.json?api-key=UO0KtPw9TJHhMgofDtUHBKCzivb20tkN'


# Retrieve page with the requests module
response = requests.get(url)

result = json.loads(response.content)

results = result['results']
results = [{'api': 'most_viewed' ,'title': x['title'], 'published_date': x['published_date'], 'adx_keywords': x['adx_keywords'].split(';')} for x in results]

collection.insert_many(results)

articles = db.articles2.find()
for a in articles:
    print(a)










