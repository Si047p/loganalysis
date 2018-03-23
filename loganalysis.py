# Python 3.5

import psycopg2

db = psycopg2.connect("dbname=news")
c = db.cursor()
c.execute(
  "select articles.title,count(*) as p_views from log join articles\
  on log.path ~ articles.slug group by articles.title order by p_views desc;")
mostpopular = c.fetchall()
print("Most Popular Articles")
for i in mostpopular:
    print(i)
c.close()

db = psycopg2.connect("dbname=news")
c = db.cursor()
c.execute(
  "select authors.name,count(*) as num from log join articles\
  on log.path ~ articles.slug join authors on authors.id = articles.author \
  group by authors.name order by num desc;")
mostpopular = c.fetchall()
print("Most Popular Article Authors")
for i in mostpopular:
    print(i)
db.close()

db = psycopg2.connect("dbname=news")
c = db.cursor()
c.execute(
  "select to_char(time, 'Mon DD, YYYY')as Date,\
  to_char(100*((SUM(CASE WHEN status = '404 NOT FOUND' THEN 1 ELSE 0 END))/\
  count(status)::numeric),'99D99%') as Error from log group by Date \
  having 1<(100*((SUM(CASE WHEN status = '404 NOT FOUND' THEN 1 ELSE 0 END))/\
  count(status)::numeric));")
perc_error = c.fetchall()
print("Days Experiencing > 1% in Page Errors")
for i in perc_error:
    print(perc_error)
db.close()
