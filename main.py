from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/gcp')
def gcp():
   return render_template('gcp.html')   

@app.route('/opengles3')
def opengles3():
   return render_template('opengles3.html')


@app.route('/questions')
def questions():
   return render_template('questions.html')


if __name__ == '__main__':
   app.run()