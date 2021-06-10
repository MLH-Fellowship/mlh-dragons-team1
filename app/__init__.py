import os
from flask import Flask, render_template, send_from_directory
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))


@app.route('/blogs')
def blog_page():
    return render_template('blog.html')


@app.route('/projects')
def project_page():
    return render_template('project.html')


@app.route('/team')
def team_page():
    return render_template('team.html')
