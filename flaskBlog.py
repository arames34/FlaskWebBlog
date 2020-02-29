from flask import Flask, render_template, url_for

app = Flask(__name__)

posts =[
{
    'author': "Arvind Ramesh",
    'title' : "Hello World Its Arvind",
    'content': 'Written by Arvind',
    'date_posted': 'Feb 28, 2020'
}
,
{
    'author': "Sakshi Ramesh",
    'title' : "Hello World Its Sakshi",
    'content': 'Written by Sakshi',
    'date_posted': 'Feb 29, 2020'
}
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/sellerLogin')
def sellerLogin():
    return render_template('sellerLogin.html')

@app.route('/renterLogin')
def renterLogin():
    return render_template('renterLogin.html')

@app.route('/renterSignup')
def renterSignup():
    return render_template('renterSignup.html')

@app.route('/sellerSignup')
def sellerSignup():
    return render_template('sellerSignup.html')

if __name__ == '__main__':
    app.run(debug=True)
