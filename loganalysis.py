#!/usr/bin/python3
# Python 3.5

import psycopg2

db = psycopg2.connect("dbname=news")
c = db.cursor()
c.execute("""
  SELECT articles.title,count(*) AS p_views
  FROM log JOIN articles
  ON log.path = '/article/'||articles.slug
  GROUP BY articles.title
  order by p_views DESC
  LIMIT 3;
""")
mostpopular = c.fetchall()
print("\n1. What are the most popular articles of all time?")
for i in mostpopular:
    i = '- "{}" -- {} views'.format(i[0], i[1])
    print(i)
db.close()

db = psycopg2.connect("dbname=news")
c = db.cursor()
c.execute("""
  SELECT authors.name,count(*) AS num
  FROM log JOIN articles
  ON log.path = '/article/'||articles.slug
  JOIN authors ON authors.id = articles.author
  GROUP BY authors.name
  ORDER BY num DESC;
""")
mostpopular = c.fetchall()
print("\n2. Who are the most popular article authors of all time?")
for i in mostpopular:
    i = "- {} -- {} views".format(i[0], i[1])
    print(i)
db.close()

db = psycopg2.connect("dbname=news")
c = db.cursor()
c.execute("""
  SELECT to_char(time, 'Mon DD, YYYY')as Date,
  to_char(100*((SUM(CASE WHEN status = '404 NOT FOUND' THEN 1 ELSE 0 END))/
  count(status)::numeric),'99D99%') AS Error
  FROM log
  GROUP BY Date
  HAVING 1<(100*((SUM(CASE WHEN status = '404 NOT FOUND' THEN 1 ELSE 0 END))/
  count(status)::numeric));
""")
perc_error = c.fetchall()
print("\n3. On which days did more than 1% of requests lead to errors?")
for i in perc_error:
    i = "- {} -- {} Errors".format(i[0], i[1])
    print(i, "\n")
db.close()
