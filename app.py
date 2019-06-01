from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author': 'person 1',
        'title': 'title 1',
        'content': 'major content',
        'date_posted': 'Fri 30 May 2010'
    },
    {
        'author': 'person 222',
        'title': 'title 222',
        'content': 'major content 22',
        'date_posted': 'Fri 30 JUN 22'
    },
    {
        'author': 'person 333',
        'title': 'title 333',
        'content': 'major content 33',
        'date_posted': 'Fri 30 FEB 20133'
    }
]

@app.route('/')
def home():
    return render_template('home.html', posts = posts, title = 'Home Page')



@app.route('/about')
def about():
    return render_template('about.html', title = 'About page')



if __name__ == '__main__':
    app.run()
