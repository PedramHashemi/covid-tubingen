from flask import Flask
from scraper import scraper

app = Flask(__name__)


@app.route('/')
def index():
    return scraper()


if __name__ == "__main__":
    app.run(debug=True)
