from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)
dictionary = {
    'landsdel': ['Götaland', 'Götaland', 'Götaland', 'Svealand', 'Svealand', 'Norrland', 'Norrland', 'Norrland',
                 'Norrland', 'Norrland'],
    'landskap': ['Östergötland', 'Östergötland', 'Västergötland', 'Södermanland', 'Södermanland', 'Norrbotten',
                 'Gästrikland', 'Ångermanland', 'Ångermanland', 'Ångermanland'],
    'stad': ['Linköping', 'Motala', 'Mjölby', 'Mariefred', 'Nyköping', 'Piteå', 'Sandviken', 'Sollefteå', 'Kramfors',
             'Örsnköldsvik']
}
my_dict = {
    "Måndag": [1, 8, 15, 22],
    "Tisdag": [2, 9, 16, 23],
    "Onsdag": [3, 10, 17, 24],
    "Torsdag": [4, 11, 18, 25],
    "Fredag": [5, 12, 19, 26],
    "Lördag": [6, 13, 20, 27],
    "Söndag": [7, 14, 21, 28]
}
names = ["Adam", "Eva", "Karl", "Lisa", "Olle", "Anna", "Bertil", "Cecilia", "Daniel", "Erika"]

df = pd.DataFrame(dictionary)
html = df.to_html(classes='table')
df_dates = pd.DataFrame(my_dict)
calender = df_dates.to_html(classes='table')


@app.route('/')
def index():
    return render_template('template.html', data=html, calender=calender, names=names)
