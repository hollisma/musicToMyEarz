from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
  return render_template('home.html')

@app.route('/analyze', methods=['POST', 'GET'])
def analyze():
  if request.method == 'POST':
    features = []

    """ get features from request.form[]
        analyze stuff """
        
    return render_template('output.html', features=features)
    # return redirect(url_for('output.html', features=features))
  elif request.method == 'GET':
    features = []

    """ get features from request.args.get() """

    return render_template('output.html', features=features)
    # return redirect(url_for('output.html', features=features))


# Below are just test routes

@app.route('/hello/<name>')
def hello(name):
  # return 'Hello %s!' % name
  return render_template('hello.html', name=name)

@app.route('/')
def login():
  return render_template('login.html')

@app.route('/action-login', methods=['POST', 'GET'])
def action_login():
  if request.method == 'POST':
    user = request.form['name']
    return redirect(url_for('hello', name=user))
  elif request.method == 'GET':
    user = request.args.get('name')
    return redirect(url_for('hello', name=user))

if __name__ == '__main__':
  app.run()
