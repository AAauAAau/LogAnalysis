# Log Analysis
This is a project that has been developed in the course of the Udacity FullstackWeb-Developer Nanodegree. It is a reporting tool writen in Python3 for a    database with the name **news**.

## Features
The following three questions are answered by the LogAnalysis tool:
  - What are the most popular three articles of all time?
  - Who are the most popular article authors of all time?
  - On which days did more than 1% of requests lead to errors?


## Installation

Log Analysis requires a instance of [Postgres](https://www.postgresql.org/) on the local maschine and a instance of the given **news** database. Use the following command to fill up the database with the content of the [newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) script.
```sh
psql -d news -f newsdata.sql
```
Install the follwing python dependencies.
```sh
$ pip install psycopg2
```
## How to run ?
Just run the LogAnalysis.py script 
```sh
$python LogAnalysis.py
```
## License
MIT
