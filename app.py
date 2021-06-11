from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", page='HOME')

@app.route('/about')
def about():
    return render_template("about.html", page='ABOUT')

@app.route('/menu')
def menu():
    return render_template("menu.html", page='MENU')

@app.route('/where')
def where():
    return render_template("where.html", page='WHERE')




if __name__ == '__main__':
    app.run()
