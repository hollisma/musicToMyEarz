# musicToMyEarz

## About this Project

We've all had amazing song ideas, but it's hard to actually write a song and see how the idea does, so we built this app using 200+ songs from Spotify and ML to tell you how popular your song will be.

## Setup / Running
First install flask, numpy, pandas, joblib, and scikit-learn. 

Next, run 
```bash
export FLASK_APP=main.py
export FLASK_ENV=development
python3 rand_forest.py
flask run
```
to run and have flask automatically refresh. Now, go to [localhost:5000](localhost:5000). The web application should appear.

Note: Before doing `flask run`, run `python3 rand_forest.py`. The trained RandomForestRegressor will be dumped on disk as a pickle file with joblib. Once the rand_forest.joblib file is on disk, the code will be able to predict the popularity of user input.

## Dataset
Dataset source: [https://www.kaggle.com/zaheenhamidani/ultimate-spotify-tracks-db](https://www.kaggle.com/zaheenhamidani/ultimate-spotify-tracks-db)

Description of Features: [https://developer.spotify.com/documentation/web-api/reference/tracks/get-audio-features/](https://developer.spotify.com/documentation/web-api/reference/tracks/get-audio-features/)

## Links
 - [Demo Video](https://www.youtube.com/watch?v=KLZYMpGFEXo)
 - [Devpost](https://devpost.com/software/musictomyearz-fwqpz7)
 - [How popularity score is determined](https://community.spotify.com/t5/Content-Questions/Artist-popularity/td-p/4415259)