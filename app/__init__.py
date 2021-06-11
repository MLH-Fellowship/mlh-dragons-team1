import os
from flask import Flask, render_template, send_from_directory, json, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', title="MLH DRAGON BLOG", url=os.getenv("URL"))


@app.route("/home")
def index():
    return render_template('index.html', title="MLH DRAGON BLOG", url=os.getenv("URL"))


# so we don't have to always go through environment variables
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


@app.route('/blogs')
def blog_page():
    dir = os.path.realpath(os.path.dirname(__file__))
    json_dir = os.path.join(dir, "static/data", "blogs.json")
    data = json.load(open(json_dir))
    return render_template('blogs.html', blogs=data['blogs'])


@app.route('/showblog')
def showblog():
    id = int(request.args.get('id'))

    dir = os.path.realpath(os.path.dirname(__file__))
    json_dir = os.path.join(dir, "static/data", "blogs.json")
    data = json.load(open(json_dir))
    blogs = data

    blog = blogs["blogs"][id]
    print(blog)
    return
    # return render_template('showblog.html', blog=blog)


@app.route('/projects')
def project_page():
    return render_template('project.html')


@app.route('/team')
def team_page():
    return render_template('team.html', title="Team Dragon's Den")
