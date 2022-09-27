from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

posts = [
    {
        'author': {
            'username': 'test-user'
        },
        'title': '첫 번째 포스트',
        'content': '첫 번째 포스트 내용입니다.',
        'date_posted': datetime.strptime('2022-09-25', '%Y-%m-%d')
    },
    {
        'author': {
            'username': 'test-user'
        },
        'title': '두 번째 포스트',
        'content': '두 번째 포스트 내용입니다.',
        'date_posted': datetime.strptime('2022-09-27', '%Y-%m-%d')
    },
]
posts = []


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/project")
def project():
    return render_template("project.html")


@app.route("/blog")
def blog():
    return render_template("blog.html", posts=posts)


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()