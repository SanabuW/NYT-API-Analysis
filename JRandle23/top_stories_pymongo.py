from bs4 import BeautifulSoup
import requests
import pymongo
import json

# Establish connection 
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# Define database and collection
db = client.top_stories_nyt
collection = db.business

# URL of page to be scraped
business_url = "https://api.nytimes.com/svc/topstories/v2/business.json?api-key=WCneLj9e31CN4wBTLqA7RxndRuHC10eZ"

# Retrieve Business top stories 
response = requests.get(business_url)

# Loas results as json document
result = json.loads(response.content)
results = result['results']
results["des_facet"] = results["des_facet"].to_str()
results = [{'api': 'topstories' ,'title': x['title'], 'published_date': x['published_date'], "des_facet": x["des_facet"].split(";")} for x in results]

# Add results to business collection 
collection.insert_many(results)

# ---------------------------------------- #
# POLITICS
db = client.top_stories_nyt
collection = db.politics

# Politics top stories url
politics_url = "https://api.nytimes.com/svc/topstories/v2/politics.json?api-key=WCneLj9e31CN4wBTLqA7RxndRuHC10eZ"

# Retrieve Politics top stories 
response = requests.get(politics_url)

# Load results as json document
result = json.loads(response.content)
results = result['results']
results = [{'api': 'topstories' ,'title': x['title'], 'published_date': x['published_date']} for x in results]

# Add results to politics collection 
collection.insert_many(results)

# ---------------------------------------- #
# US 
db = client.top_stories_nyt
collection = db.us

# US top stories URL
us_url = "https://api.nytimes.com/svc/topstories/v2/us.json?api-key=WCneLj9e31CN4wBTLqA7RxndRuHC10eZ"

# Retrieve US top stories 
response = requests.get(us_url)

# Load results as json document
result = json.loads(response.content)
results = result['results']
results = [{'api': 'topstories' ,'title': x['title'], 'published_date': x['published_date']} for x in results]

# Add results to US collection 
collection.insert_many(results)

# ---------------------------------------- #
# TECHNOLOGY
db = client.top_stories_nyt
collection = db.technology 

# Technology top stories URL
tech_url = "https://api.nytimes.com/svc/topstories/v2/technology.json?api-key=WCneLj9e31CN4wBTLqA7RxndRuHC10eZ"

# Retrieve Technology top stories 
response = requests.get(tech_url)

# Load results into a json document 
result = json.loads(response.content)
results = result['results']
results = [{'api': 'topstories' ,'title': x['title'], 'published_date': x['published_date']} for x in results]

# Add results to technology collection 
collection.insert_many(results)

# ---------------------------------------- #
# OPINION
db = client.top_stories_nyt
collection = db.opinions

# Opinion top stories URL
opinion_url = "https://api.nytimes.com/svc/topstories/v2/opinion.json?api-key=WCneLj9e31CN4wBTLqA7RxndRuHC10eZ"

# Retrieve Opinion top stories 
response = requests.get(opinion_url)

# Load results into a json document 
result = json.loads(response.content)
results = result['results']
results = [{'api': 'topstories' ,'title': x['title'], 'published_date': x['published_date']} for x in results]

# Add results to Opinion collection 
collection.insert_many(results)

