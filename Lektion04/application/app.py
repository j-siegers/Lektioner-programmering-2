import pandas as pd
from flask import Flask, render_template, request
import urllib.request
import ssl
import json
import pandas

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/form')
def form():
    return render_template('form.html')


@app.post('/api')
def api_post():
    year = request.form["year"]
    country_code = request.form["countrycode"]
    context = ssl._create_unverified_context()
    data_url = f'https://date.nager.at/api/v3/PublicHolidays/{year}/{country_code}'
    try:
        json_data = urllib.request.urlopen(data_url, context=context).read()
        data = json.loads(json_data)
        df = pd.DataFrame(data)
        table_data = df.to_html(columns=["date", "localName"], classes="table p-5", justify="left")

    except:
        print('Ett fel uppstod')
        return render_template('index.html')

    return render_template('index.html', data=table_data)
