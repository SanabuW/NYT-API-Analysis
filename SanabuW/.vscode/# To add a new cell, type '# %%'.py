# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pymongo
import requests
import json
import time
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import sys
sys.path.append("../common")
from api_keys_local_SW import nyt_API_key


# %%
# connect to mongodb database
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)


# %%
# create reflections and local classes
db = client.gs_search_db
collection = db.gs_articles


# %%
# define url/search params
# set up utilities/params
# pass API key
api_key = nyt_API_key
search_terms = ["gamestop", "election", "covid", "mars", "tesla"]
begin_date = "20201101"
end_date = "20210220"
current_page_counter = 0
page_count_limit = 30
searchCompleteVar = False
search_term_count = 1

# Request loop
for term in search_terms:
    search_post = {
        }
    articles_list = []
    current_page_counter = 0
    for p in range(0,30):
        # sleep to follow API rules
        time.sleep(6)
        # defining url
        url = f'https://api.nytimes.com/svc/search/v2/articlesearch.json?q={term}&begin_date={begin_date}&end_date={end_date}&page={current_page_counter}&api-key={api_key}'

        # set up exception handling for the call
        try:
            # make request and turn into json object
            requestObject = requests.get(url)
            response = json.loads(requestObject.text)
            print()
            print("The status code is {}".format(requestObject.status_code) + " for page " + str(current_page_counter) + " of: " + term)
            print(requestObject.url[0:-41])
        except:
            # on call error, break from current search term loop and move to next search term
            print()
            print("Invalid results. Moving to next request.")            
            current_page_counter = 0
            break

        if requestObject.status_code == 200:
            if response["response"]["docs"] != []:
            #for each article's docs section
                print(f'Getting responses...')
                for art in response["response"]["docs"]:
                    articles_list.append(art)
                current_page_counter += 1
            else:
                print(f'End of results. Starting new search term query')
                current_page_counter = 0
                break                  
            # check if requests are at their limit for search term
            if current_page_counter == page_count_limit:
                searchCompleteVar = False
                print(f'At final page allowed.')
                current_page_counter = 0
                break

    #add search term
    search_post["search_term"] = term
    #add articles list
    search_post["articles"] = articles_list
    #get hits number
    search_post["hits"] = response["response"]["meta"]["hits"]
    #add to collection
    collection.insert_one(search_post)

    #prep for next search term
    search_term_count += 1
    #move to next search term
    current_page_counter = 0
    #add if clause for 
    print(f'Moving to search term {search_term_count}.')


# %%



