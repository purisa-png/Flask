from flask import Flask, render_template, request
import sqlite3
from sqlite3 import Error

app = Flask(__name__)
DATABASE = "Dances.db"

def create_connection(db_file):
    """
    Creates a connection to the database
    :parameter db_file - the name of the file
    :returns connection - a connection to the database
    """

    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as e:
        print(e)
    return None

tags = [
    ["color", "Changes the text colour"],
    ["font-size", "Changes the text size"],
    ["background-color", "Changes the background colour"]
]

@app.route('/')
def render_home():
    return render_template('index.html')

@app.route('/webpages')
def render_webpages():
    query = "SELECT dance_name, description FROM Dances WHERE type = 'HTML'"
    con = create_connection(DATABASE)
    cur = con.cursor()

    # Query the DATABASE
    cur.execute(query)
    tag_list = cur.fetchall()
    con.close()

    print(tag_list)
    return render_template('webpages.html', tags=tag_list)

@app.route('/styles')
def render_styles():
    return render_template('styles.html', tags=tags)


@app.route('/search', methods=['POST'])
def search():
    search_term = request.form['search']

    query = """
    SELECT dance_name, description
    FROM Dances
    WHERE dance_name LIKE ?
    OR description LIKE ?
"""

    con = create_connection(DATABASE)
    cur = con.cursor()

    cur.execute(query, ('%' + search_term + '%', '%' + search_term + '%'))
    results = cur.fetchall()

    con.close()

    return render_template('search.html', results=results, search_term=search_term)

@app.route('/test')
def test():
    con = create_connection(DATABASE)
    cur = con.cursor()

    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cur.fetchall()

    con.close()
    return str(tables)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

