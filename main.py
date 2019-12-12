"""AlayaNotes

Usage:
  main.py [run]
  main.py initdb
"""
from docopt import docopt
import os
import sqlite3

from alayatodo import app
from alayatodo import db

def _run_sql(filename):
    try:
        db_connection = db.connect_db()
        fullPath = os.path.join(os.path.dirname(__file__), filename)
        if os.path.exists(fullPath):
            with open(fullPath, 'r') as f:
                db_connection.executescript(f.read())
        
    except Exception as ex:
        print(ex.__str__())
        os._exit(1)

if __name__ == '__main__':
    args = docopt(__doc__)
    if args['initdb']:
        _run_sql('resources/database.sql')
        _run_sql('resources/fixtures.sql')
        print("AlayaTodo: Database initialized.")
    else:
        app.run(use_reloader=True)
