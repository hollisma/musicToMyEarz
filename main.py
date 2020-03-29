from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
  return render_template('home.html')

@app.route('/analyze', methods=['POST', 'GET'])
def analyze():
  if request.method == 'POST':
    features = {}

    """ get features from request.form[]
        analyze stuff """
    features['name'] = request.form['name'] + ', ' if request.form['name'] != None else ''
        
    return render_template('output.html', features=features)
    # return redirect(url_for('output.html', features=features))
  elif request.method == 'GET':
    features = []

    """ get features from request.args.get() """

    return render_template('output.html', features=features)
    # return redirect(url_for('output.html', features=features))

@app.route('/hello/<name>')
def hello(name):
  return render_template('hello.html', name=name)

if __name__ == '__main__':
  app.run()
