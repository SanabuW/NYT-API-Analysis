CREATE TABLE articles_gs_app3 (	
	id SERIAL PRIMARY KEY,
	search_term VARCHAR,
	abstract VARCHAR,
	web_url VARCHAR,
	main_headline VARCHAR,
	keywords VARCHAR,
	pub_date VARCHAR,
	document_type VARCHAR,
	nyt_id VARCHAR,
	word_count INT,
	search_hits INT,
	week_ending_in VARCHAR
);


-- Import data through Table Import/Export wizard with settings:
-- Header: Yes
-- All other settings are on default