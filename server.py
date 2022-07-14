from flask import Flask, render_template, session, redirect

app = Flask(__name__)

app.secret_key="keep it a secret"

@app.route('/')
def index():
    if "count" not in session:
        session["count"] = 0
    else:
        session['count'] += 1
    return render_template("index.html")

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

@app.errorhandler(404)
def check(error):
    return f"Page not found"

if __name__=="__main__":
    app.run(debug=True)