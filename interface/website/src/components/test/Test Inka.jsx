import React, { useState } from 'react';
import axios from 'axios';
import './Prediction.css';

const TestInka = () => {
  const [result, setLoadedData] = useState([]);

  const requestData = () => {
    axios
      .get('http://127.0.0.1:8000/testinka')
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
        <h1 className="gradient-text">Test Inka</h1>
        <h4> This is the private test region for Inka and should not be removed. </h4>
        <button className="solarscore__prediction-button" onClick={requestData}>Test Request</button>
        <div className='item-container'>
          Loaded Data: {result.message} {result.data}
        </div>
      </div>
    </div>
  )
};

export default TestInka;
