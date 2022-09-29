from flask import Flask, render_template
from datetime import datetime
import pandas as pd

app = Flask(__name__)


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
    df = pd.read_csv("blog_content.csv")
    posts = []

    # df.iterrows = 한줄씩 읽음
    for idx, row in df.iterrows():
        posts.append({
            'author': {'username': row["username"]},
            'title': row["title"],
            'content': row["content"],
            'date_posted': datetime.strptime(row["date_posted"], '%Y-%m-%d')
        })

    return render_template("blog.html", posts=posts)


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()