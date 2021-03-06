from flask import Flask, render_template, redirect, url_for, request
import predict

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
    features['name'] = request.form['name'] + ', ' if request.form['name'].strip() != "" else ''
    features['genre'] = request.form['genre']
    features['acousticness'] = int(request.form['acousticness'])
    features['danceability'] = request.form['danceability'] 
    features['duration'] = float(request.form['duration']) * 1000 if request.form['duration'].strip() != "" else 0
    features['energy'] = int(request.form['energy']) 
    features['instrumentalness'] = int(request.form['instrumentalness']) 
    features['key'] = request.form['key']
    features['liveness'] = int(request.form['liveness']) 
    features['loudness'] = int(request.form['loudness']) 
    """
    If mode is 1 (major), then ('mode', 1) is in request.form dict
    If mode is 0 (minor), then 'mode' is not a key in the request.form dict
    """
    if 'mode' in request.form:
      features['mode'] = request.form['mode']
    else:
      features['mode'] = 0
    features['speechiness'] = int(request.form['speechiness']) 
    features['tempo'] = int(request.form['tempo']) 
    """
    Time sig: x/4 -> x
    """
    features['time_signature'] = int(request.form['time_signature'])
    features['valence'] = int(request.form['valence']) 

    
    predict_popularity_value = str(predict.predict_pop(features))
    return render_template('output.html', features = features, popularity=predict_popularity_value)
    # return redirect(url_for('output.html', features=features))
  elif request.method == 'GET':
    features = []

    """ get features from request.args.get() """

    return render_template('output.html', features=features)
    # return redirect(url_for('output.html', features=features))

if __name__ == '__main__':
  app.run()
