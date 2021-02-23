# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func
import pandas as pd
import pymongo

# %% [markdown]
# # Extraction

# %%



# %%
engine = create_engine('postgresql://postgres:pgadmin@localhost/nyt_db')
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)


# %%
inspector = inspect(engine)
tables = inspector.get_table_names()
tables


# %%
table_cols_obj = inspector.get_columns("articles_gs_app3")
table_col_list = []
[table_col_list.append(x["name"]) for x in table_cols_obj]
table_col_list


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



# %%
full_result = gs_articles_response.find()

print(full_result[0]["search_term"])
print(full_result[0]["hits"])
print(full_result[0]["articles"][0]["abstract"])
print(full_result[0]["articles"][0]["web_url"])
print(full_result[0]["articles"][0]["headline"]["main"])
print(full_result[0]["articles"][0]["keywords"][0]["value"])
print(full_result[0]["articles"][0]["pub_date"])
print(full_result[0]["articles"][0]["document_type"])
print(full_result[0]["articles"][0]["type_of_material"])
print(full_result[0]["articles"][0]["_id"])
print(full_result[0]["articles"][0]["word_count"])




# %%
counter_var = 0
stop_var = 1

for search_term in full_result:
    if stop_var > counter_var:
        #for each article
        for article in search_term["articles"]:
            search_term_var = article["abstract"]
            web_url_var = article["web_url"]
            headline_var = article["headline"]["main"]
            pub_date_var = article["pub_date"]
            key_words_list = []
            for kw in article["keywords"]:
                keywords_var = key_words_list .append(kw["value"])
            key_words_tup = tuple(keywords_var)
            document_type_var = article["document_type"]
            type_of_material_var = article["type_of_material"]
            _id_var = article["_id"]
            word_count_var = article["word_count"]

            print(search_term_var)
            #make individual queries
        counter_var +=1
    break


# %%
print(key_words_tup)


# %%



