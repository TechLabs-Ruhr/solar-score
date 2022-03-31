import React, { useState } from 'react';
import axios from 'axios';
import './Test Styling.css';

const TestKatharina = () => {
  const [result, setLoadedData] = useState([]);

  const requestData = () => {
    axios
      .get('http://127.0.0.1:8000/testkatharina')
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
        <h1 className="gradient-text">Test Katharina</h1>
        <h4> This is the private test region for Katharina and should not be removed. </h4>
        <button className="solarscore__test-button" onClick={requestData}>Test Request</button>
        <div className='item-container'>
          Loaded Data: {result.message} {result.data}
        </div>
      </div>
    </div>
  )
};

export default TestKatharina;
