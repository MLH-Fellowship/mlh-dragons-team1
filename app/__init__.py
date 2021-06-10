import os
from flask import Flask, render_template, send_from_directory
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))


# so we don't have to always go through environment variables
if __name__ == '__main__':
    app.run(debug=True)


@app.route('/blogs')
def project_page():
    return render_template('blog.html')


@app.route('/projects')
def project_page():
    return render_template('project.html')


@app.route('/team')
def project_page():
    return render_template('team.html')
