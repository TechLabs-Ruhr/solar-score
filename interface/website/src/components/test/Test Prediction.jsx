import React, { useState } from 'react';
import axios from 'axios';
import './Test Styling.css';
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
    <div className="solarscore__test section__margin" id="test">
      <div className="solarscore__test-heading">
        <h1 className="gradient-text">Prediction Test </h1>
        <h4> This section is for testing the final layout and should not be removed. </h4>
        <button className="solarscore__test-button" onClick={requestData}>New power prediction</button>
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
      </div>
    </div>
  )
};


export default TestPrediction;