from flask import Flask, request, url_for, redirect, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/players', methods=['GET', 'POST'])
def players():
    if request.method == "POST":

        return redirect(url_for('home'))

    return render_template("/players.html")

@app.route('/teams', methods=['GET', 'POST'])
def teams():
    if request.method == "POST":

        return redirect(url_for('home'))

    return render_template("/teams.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
