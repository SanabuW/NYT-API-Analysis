# ETL-Project
      
      ###This project examined the Extract, Transform, and Load methods with the New York Times API. We explored the Archive API, Top Stories API, Article search API, and Most popular API to answer the question, “Do we like the stock?” The stock in question being, Gamestop (GME).
    ###We chose to use a No-SQL database which allows for the data to be stored in a collection. The keys of the collection were then queryable. Keys such as “Title”, “Headline”, and “keywords.”
      ###The archive API generated metadata on all of the articles within a given month. This metadata was inserted into a Mongo database. From this database, keywords such as “Gamestop” were searchable. 
    ###The Top Stories API generated metadata on all of the articles currently on the landing page for each section of the NYT.  We chose to do Business, Technology, US, Politics, and Opinion sections, where we were able to pull the title and published date information to input into MongoDB.
