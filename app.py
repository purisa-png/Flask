from flask import Flask, render_template
app = Flask(__name__)

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
    return render_template('webpages.html')

@app.route('/styles')
def render_styles():
    return render_template('styles.html', tags=tags)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)