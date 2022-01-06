from flask import Flask, render_template
from scraper import scraper
import json
import plotly
import plotly.graph_objects as go

app = Flask(__name__)


@app.route('/')
def index():
    covid_data = scraper()
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=covid_data['date'][::-1],
        y=covid_data['infected'][::-1],
        name='Infected',
        line=dict(color='firebrick', width=1)))
    fig.add_trace(go.Scatter(
        x=covid_data['date'][::-1],
        y=covid_data['intensive'][::-1],
        name='Intensive',
        mode='lines',
        line=dict(color='royalblue', width=1)))

    fig.show()
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('index.html', plot=graphJSON)


if __name__ == "__main__":
    stop = 1
    app.run(debug=True)
