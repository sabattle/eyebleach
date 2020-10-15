from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def get_dog():
    res = requests.get('https://random.dog/woof.json')
    image_url = res.json()['url']
    return render_template('index.html', image=image_url)

if __name__ == '__main__':
    app.run(debug=True)
