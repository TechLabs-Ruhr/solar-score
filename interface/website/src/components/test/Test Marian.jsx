import React, { useState } from 'react';
import axios from 'axios';
import './Test Styling.css';

const TestMarian = () => {
  const [result, setLoadedData] = useState([]);

  const requestDataMarian = () => {
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
      <div className="solarscore__test-heading">
        <h1 className="gradient-text">Test Marian</h1>
        <h4> This is the private test region for Marian and should not be removed. </h4>
        <button className="solarscore__test-button" onClick={requestDataMarian}>Test Request</button>
        <div className='item-container'>
          Loaded Data: {result.message} {result.data}
          <div dangerouslySetInnerHTML={{ __html: result.data }} />
        </div>
      </div>
    </div>
  )
};

export default TestMarian;