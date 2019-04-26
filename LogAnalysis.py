#!/usr/bin/env python3
# Log Analysis of the news Database
import psycopg2

DBNAME = "dbname='news'user='postgres'"

if __name__ == '__main__':
    try:
        db = psycopg2.connect(DBNAME)
    except Exception:
        print("I am unable to connect to the database.")

    print("     Log Analysis    ")
    print("*********************")
    c = db.cursor()
    c.execute("SELECT (SELECT title from articles "
              + "WHERE concat('/article/',slug) LIKE path) as title,"
              + "COUNT(*)as amount from log "
              + "WHERE path LIKE '/article/%' GROUP BY path "
              + "ORDER BY COUNT(*) DESC limit 3")
    topArticle = c.fetchall()
    # Task 1
    print("")
    print("Top 3 Articles:")
    print("--------------------------------------")
    for article, views in topArticle:
        print('{} - {} views'.format(article, views))
    # Task 2
    c.execute("SELECT au.name,SUM (amount) AS total "
              + "FROM (SELECT path, COUNT(*)as amount from log "
              + "WHERE path LIKE '/article/%' GROUP BY path "
              + "ORDER BY COUNT(*) desc) as b,authors as au, articles as ar "
              + "WHERE concat('/article/',ar.slug) "
              + "LIKE b.path and ar.author=au.id "
              + "GROUP BY au.name order by SUM (amount) desc")
    topAuthor = c.fetchall()
    print("")
    print("Top Authors:")
    print("--------------------------------------")
    for author, views in topAuthor:
        print('{} - {} views'.format(author, views))

    # Task 3
    c.execute("SELECT a._date as _date,"
              + "(a.error*1.0/b.ok)*100.0 as requestsErrors "
              + "from (SELECT DATE(time) as _date, count(*) as error "
              + "from log WHERE status!='200 OK' GROUP BY DATE(time))as a "
              + "join (SELECT DATE(time) as _date, count(*) as ok from log "
              + "WHERE status='200 OK' GROUP BY DATE(time)) as b "
              + "on a._date=b._date "
              + "WHERE ((a.error*1.0/b.ok)*100.0)>1.0")
    requestsErrorsArticles = c.fetchall()
    print("")
    print("Days with a Requests errors over 1%:")
    print("--------------------------------------")
    for date, errorInPercentage in requestsErrorsArticles:
        print(date.strftime("%b %d, %Y")+" - "+'%.1f' %
              errorInPercentage+"% errors")

    db.close()
