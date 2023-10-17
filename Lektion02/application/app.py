from flask import Flask

app = Flask(__name__)

picture = '<img src="https://c-mw.niceshops.com/upload/image/product/large/default/66440_9a8f2917.256x256.jpg">'

page = f'''<html>
<head><title>Välkommen hem</title></head>
<body>
<h1>Hej och välkommen till hemsidan</h1>
{picture}
</body>
</html>

'''


@app.route('/')
def index():
    return page
