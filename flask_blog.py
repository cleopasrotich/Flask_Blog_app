from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'title': 'Blog Post 1',
        'author': 'Cleopas Rotich',
        'content': 'First post posted',
        'date_posted': 'January 7th, 2019'
    },
    {
        'title': 'Blog Post 2',
        'author': 'Corey Schaffer',
        'content': 'Second post posted',
        'date_posted': 'January 7th, 2019'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == "__main__":
    app.run(debug=True)
