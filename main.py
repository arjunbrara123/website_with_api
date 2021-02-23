from flask import Flask, render_template, request
import requests

app = Flask(__name__)
name_api_url = "https://api.nationalize.io/"

def name_from(name):
    return requests.get(url=name_api_url, params={"name": name}).json()['country']

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        print(request.form['name'])
        return render_template('index.html', sources=name_from(request.form['name']))
    return render_template('index.html', sources="")

if __name__ == "__main__":
    app.run(debug=True)
