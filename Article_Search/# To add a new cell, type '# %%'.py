# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
import pandas as pd
import pymongo
from pprint import pprint
from datetime import datetime, timedelta


# %%
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)


# %%
db = client.gs_search_db
gs_articles_response = db.gs_articles
type(gs_articles_response)


# %%
full_result = gs_articles_response.find()


# %%
engine = create_engine('postgresql://postgres:pgadmin@localhost/nyt_db')
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)


# %%
Base.classes.keys()


# %%
sql_table = Base.classes.articles_gs_app3


# %%
session = Session(engine)
#for each search term
for search_term in full_result:
    search_term_var = search_term["search_term"]
    hits_var = search_term["hits"]
        #for each article
    for article in search_term["articles"]:
        abstract_var = article["abstract"]
        web_url_var = article["web_url"]
        headline_var = article["headline"]["main"]
        pub_date_var = article["pub_date"]
        key_words_list = []
        for kw in article["keywords"]:
            key_words_list.append(kw["value"])
        if key_words_list == []:
            key_words_tup = "None"
        else:
            key_words_tup = tuple(key_words_list)
        document_type_var = article["document_type"]
        type_of_material_var = article["type_of_material"]
        _id_var = article["_id"]
        word_count_var = article["word_count"]
        # convert pub_date to week ending in date
        date_var = datetime.fromisoformat(pub_date_var[0:-5]).date()
        week_start = date_var - timedelta(days = date_var.weekday())
        week_end_date = week_start + timedelta(days=6)
        # build object to add to sql table
        post_object = sql_table(
            search_term = search_term_var,
            abstract = abstract_var,
            web_url = web_url_var,
            main_headline = headline_var,
            keywords = key_words_tup,
            pub_date = pub_date_var,
            document_type = document_type_var,
            type_of_material = type_of_material_var,
            nyt_id = _id_var,
            word_count = word_count_var,
            search_hits = hits_var,
            week_ending_in = week_end_date)
            # Add object
        session.add(post_object)
    print("Posting")
    session.commit()
    print("Moving to next term")
# end session
session.close()


# %%



