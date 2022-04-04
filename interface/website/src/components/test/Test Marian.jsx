import React, { useState } from 'react';
import axios from 'axios';
import './Test Styling.css';
import Plot from 'react-plotly.js'

const TestMarian = () => {
  const [result, setLoadedData] = useState([]);

  const requestData = () => {
    axios
      .get('http://127.0.0.1:8000/testmarian')
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
      <div className="solarscore__test-content">
        <h1 className="gradient-text">Test Marian</h1>
        <h4> This is the private test region for Marian and should not be removed. </h4>
        <button className="solarscore__test-button" onClick={requestData}>Test Request</button>
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
                color: 'rgb(10, 27, 59)',
                opacity: 1,
                size: 5,
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
      </div>
    </div>
  )
};

export default TestMarian;