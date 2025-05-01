# Goodreads Ratings Migration Assistant

This script was written to assist in migrating ratings from Goodreads to another service/system manually. In many cases, said service will provide a tool to automatically parse this for you and you should use that.

Otherwise, this script will parse your exported Goodreads history and present your previously read books, one author at a time, and the scores assigned to them. You then have the option of marking that author as migrated or not.

## Pre-requisites

Export your library via [the export page.](https://www.goodreads.com/review/import). Save this as `goodreads_library_export.csv`.

## Usage

First, run `python3 create-db.py` to generate an sqlite database of your exported library. This will be saved as `goodreads_export.db`.

Then, simply call `python3 get-scores.py` to pull a list of books with the format `(${AUTHOR}, ${TITLE}, ${SCORE})`. To remove these from the database, type `y` and hit enter. Anything else will not modify the database.

## Future Work

Future improvements may involve optionally outputting the reviews, if available, and improving the command line interface.

Also there is absolutely no error handling in this script. Use at your own risk.

