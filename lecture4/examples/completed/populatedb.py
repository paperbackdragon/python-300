import os
import sys
import sqlite3
from utils import AUTHORS_BOOKS

DB_FILENAME = 'books.db'
DB_IS_NEW = not os.path.exists(DB_FILENAME)

author_insert = "INSERT INTO author (name) VALUES(?);"
author_query = "SELECT * FROM author;"
book_query = "SELECT * FROM book;"
book_insert = """
INSERT INTO book (title, author) VALUES(?, (
    SELECT authorid FROM author WHERE name=? ));
"""


def show_query_results(conn, query):
    cur = conn.cursor()
    cur.execute(query)
    had_rows = False
    for row in cur.fetchall():
        print row
        had_rows = True
    if not had_rows:
        print "no rows returned"


def show_authors(conn):
    query = author_query
    show_query_results(conn, query)


def show_books(conn):
    query = book_query
    show_query_results(conn, query)


def populate_db(conn):
    authors = ([author] for author in AUTHORS_BOOKS.keys())
    cur = conn.cursor()
    cur.executemany(author_insert, authors)
    
    for author in AUTHORS_BOOKS.keys():
        params = ([book, author] for book in AUTHORS_BOOKS[author])
        cur.executemany(book_insert, params)


if __name__ == '__main__':
    if DB_IS_NEW:
        print "Database does not yet exist, please run `createdb` first"
        sys.exit(1)
    
    with sqlite3.connect(DB_FILENAME, isolation_level=None) as conn1:
        with sqlite3.connect(DB_FILENAME, isolation_level=None) as conn2:
            try:
                populate_db(conn1)
                print "\nauthors and books on conn2 before commit:"
                show_authors(conn2)
                show_books(conn2)
            except Exception:
                conn1.rollback()
                print "\nauthors and books on conn2 after rollback:"
                show_authors(conn2)
                show_books(conn2)
                raise
            else:
                print "\ncommitting write transactions"
                conn1.commit()
                print "\nauthors and books on conn2 after commit:"
                show_authors(conn2)
                show_books(conn2)
