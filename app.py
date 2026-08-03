from flask import Flask, render_template
import sqlite3
from sqlite3 import Error

app = Flask(__name__)
DATABASE = "tags.db"

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
    query = "SELECT tag, description from html_tags WHERE type= 'HTML'"
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

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)