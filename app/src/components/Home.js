import React from "react";

const Dashboard = () => {
  return (
    <div>
      <form action="http://localhost:5000/analyze" method="post"> 
        <h2>Welcome to MusicToMyEarz!</h2> 
        <p>Name: <input type="text" name="name" /></p> 
        <p>Genre: <input type="text" name="genre" /></p> 
        <p>Acousticness: <input type="text" name="acousticness" /></p> 
        <p>Danceability: <input type="text" name="danceability" /></p> 
        <p>Duration (in ms): <input type="text" name="duration_ms" /></p> 
        <p>Energy: <input type="text" name="energy" /></p> 
        <p>Instrumentalness: <input type="text" name="instrumentalness" /></p> 
        <p>Key: <input type="text" name="key" /></p> 
        <p>Liveness: <input type="text" name="liveness" /></p> 
        <p>Loudness: <input type="text" name="loudness" /></p> 
        <p>Mode: <input type="text" name="mode" /></p> 
        <p>Speechiness: <input type="text" name="speechiness" /></p> 
        <p>Tempo: <input type="text" name="tempo" /></p> 
        <p>Time Signature: <input type="text" name="time_signature" /></p> 
        <p>Valence: <input type="text" name="valence" /></p> 
        <p><input type="submit" value="submit" /></p> 
      </form>   
    </div>
  );
};

export default Dashboard;