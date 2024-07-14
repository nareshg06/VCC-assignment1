from flask import Flask, render_template
import random

app = Flask(__name__)

images = ["https://w7.pngwing.com/pngs/190/922/png-transparent-kubernetes-docker-devops-lxc-mongodb-github-blue-logo-symmetry-thumbnail.png"]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
