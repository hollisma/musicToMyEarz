from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

@app.route('/hello/<name>')
def hello(name):
  # return 'Hello %s!' % name
  return render_template('hello.html', name=name)

@app.route('/')
@app.route('/login')
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
