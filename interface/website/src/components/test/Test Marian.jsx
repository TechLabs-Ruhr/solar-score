import React, { useState } from 'react';
import axios from 'axios';
import './Prediction.css';
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
    <div className="solarscore__prediction section__margin" id="test">
      <div className="solarscore__prediction-content">
        <h1 className="gradient-text">Prediction Plot</h1>
        <p> This graph shows the predicted solar power outcome for the next x days in Gelsenkirchen. </p>
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

          layout={
            {
              title: 'Power Prediction',
              titlefont: { family: 'Manrope, sans-serif', size: 20, color: '#0A1B3B' },
              width: 1250,
              plot_bgcolor: 'rgb(255, 175, 64)',
              xaxis: {
                type: 'date',
                title: 'Time in [h]',
                titlefont: {
                  family: 'Manrope, sans-serif',
                  size: 18,
                  color: '#0A1B3B'
                }
              },
              yaxis: {
                title: 'Solar power in [kW]',
                titlefont: {
                  family: 'Manrope, sans-serif',
                  size: 18,
                  color: '#0A1B3B'
                }
              },
            }}
        />
        <button className="solarscore__prediction-button" onClick={requestData}>Predict</button>
      </div>
    </div>
  )
};

export default TestMarian;