from flask import Flask, request, render_template
import random
app = Flask(__name__)

lower='abcdefghijklmnopqrstuvwxyz'
upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers='1234567890'
symbols='!@#$%^&*()_+?/-'

@app.route("/", methods=['post','get'])
def hello():
    return render_template("index.html")

@app.route('/random', methods=['POST','GET'])
def random_word():
    ques = int(request.form['ques'])
    string=''
    if request.method=="POST":
        if (request.form.get('loweropt'))=='1':
            string+=lower
        if (request.form.get('upperopt'))=='1':
            string+=upper
        if (request.form.get('numopt'))=='1':
            string+=numbers
        if (request.form.get('symopt'))=='1':
            string+=symbols
    k=min(ques, len(string))
    password= ''.join(random.sample(string, k))

    return render_template("index.html", password=password)

if __name__=='__main__':
    app.run(debug=True)