ALTER TABLE articles_gs ALTER COLUMN pub_date TYPE DATE 
using to_date(pub_date, 'YYYY-MM-DD');

ALTER TABLE articles_gs ALTER COLUMN week_ending_in TYPE DATE 
using to_date(week_ending_in, 'YYYY-MM-DD');