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
          data={[
            {
              x: result.x,
              y: result.y,
              type: "scatter gl",
              fill: 'tozeroy',
              mode: 'markers',
              fillcolor: 'rgb(10, 27, 59)',
              line: {
                color: 'white',
                width: 20,
              },
              marker: {
                color: 'rgb(255, 175, 64)',
                opacity: 1,
                size: 6,
                line: {
                  color: 'white',
                  width: 2,
                }
              },
            }
          ]}
          layout={{
            width: 1250,
            plot_bgcolor: 'rgb(255, 175, 64)',
            title: 'Prediction chart',
            xaxis: {
              type: 'date',
              title: 'Future date',
              titlefont: {
                family: 'Courier New, monospace',
                size: 18,
                color: '#7f7f7f'
              },
            },
            yaxis: {
              title: 'Solar power in [kW]',
              titlefont: {
                family: 'Courier New, monospace',
                size: 18,
                color: '#7f7f7f'
              },
            },
          }}
        />
        <button className="solarscore__prediction-button" onClick={requestData}>New power prediction</button>
      </div>
    </div>
  )
};


export default TestPrediction;