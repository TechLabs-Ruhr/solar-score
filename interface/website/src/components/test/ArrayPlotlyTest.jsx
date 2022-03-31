import React, { useState } from 'react';
import axios from 'axios';
import './test.css';
import Plot from 'react-plotly.js'

const TestArray = () => {
  const [result, setLoadedData] = useState([]);

  const requestDataArray = () => {
    axios
      .get('http://127.0.0.1:8000/testarray')
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
        <button className="solarscore__test-button" onClick={requestDataArray}>Test Array</button>
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


export default TestArray;