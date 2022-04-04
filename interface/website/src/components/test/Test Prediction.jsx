import React, { useState } from 'react';
import axios from 'axios';
import './Prediction.css';
import Plot from 'react-plotly.js'

const TestPrediction = () => {
  const [result, setLoadedData] = useState([]);

  const requestData = () => {
    axios
      .get('http://127.0.0.1:8000/testprediction')
      .then((res) => {
        setLoadedData(res.data);
        console.log(res);
      })
      .catch((err) => {
        console.log(err);
      });
  };
  return (
    <div className="solarscore__prediction section__margin" id="test">
      <div className="solarscore__prediction-content">
        <h1 className="gradient-text">Prediction Plot </h1>
        <p> This section is for testing the final layout and should not be removed. </p>
        <Plot
          data={
            [
              {
                x: result.x,
                y: result.y,
                type: "scatter"
              }
            ]
          }
        />
        <button className="solarscore__prediction-button" onClick={requestData}>New power prediction</button>
      </div>
    </div>
  )
};


export default TestPrediction;