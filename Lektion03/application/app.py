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
df = pd.DataFrame(dictionary)
html = df.to_html(classes='table')


@app.route('/')
def index():
    return render_template('template.html', data=html)
