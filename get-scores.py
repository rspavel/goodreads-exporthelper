import sqlite3

sql = sqlite3.connect("goodreads_export.db")
cur = sql.cursor()

# Select an author randomly
ret = cur.execute("SELECT author FROM books ORDER BY RANDOM() LIMIT 1;")
author = ret.fetchone()[0]
# Print every book by that author
for book in cur.execute(f"SELECT author, title, score FROM books WHERE author=\"{author}\" ORDER BY title;"):
    print(book)
# Check if user wants to drop the table
resp = input("Delete selected books? (y/N)?")
# And then drop that author if the user wants to
if resp == "y":
    print(f"Deleting books by {author}")
    cur.execute(f"DELETE FROM books WHERE author=\"{author}\";")
    sql.commit()
ret = cur.execute("SELECT COUNT(*) FROM books")
titleCount = ret.fetchone()
print(f"{titleCount} books remain")

sql.close()

