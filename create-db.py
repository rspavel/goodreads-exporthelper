import csv
import sqlite3

TITLE_COL=1
AUTHOR_COL=2
SCORE_COL=7

sql = sqlite3.connect("goodreads_export.db")
cur = sql.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS books(title, author, score)")

with open('goodreads_library_export.csv', newline='') as csvfile:
    gReader = csv.reader(csvfile)
    # Dump header row
    next(gReader)
    # For every book in the dump
    for row in gReader:
        # If this book was read/scored
        if int(row[SCORE_COL]) != 0:
            title = row[TITLE_COL]
            author = row[AUTHOR_COL]
            score = row[SCORE_COL]
            cur.execute(f"INSERT INTO books (title, author, score) VALUES (\"{title}\", \"{author}\", {score});")
    sql.commit()
ret = cur.execute("SELECT COUNT(*) FROM books")
titleCount = ret.fetchone()
print(f"{titleCount} books total")
sql.close()

