import React, { useState, useEffect } from 'react';
import '../core/Prediction.css';
import axios from 'axios';
import { AgGridReact } from 'ag-grid-react';
import 'ag-grid-community/dist/styles/ag-grid.css';
import 'ag-grid-community/dist/styles/ag-theme-material.css';

const TestKatharina = () => {
  const [rowData, setRowData] = useState([]);

  const [columnDefs] = useState([
    { field: 'time' },
    { field: 'prediction' },
  ]);

  const requestData = () => {
    axios
      .get('http://127.0.0.1:8000/testkatharina')
      .then((result) => {
        setRowData(result.data);
        console.log(result);
      })
      .catch((err) => {
        console.log(err);
      });
  };

  return (
    <div className="solarscore__prediction section__margin" id="test">
      <div className="solarscore__prediction-content">
        <h1 className="gradient-text">Prediction Table</h1>
        <p> This table shows the predicted solar power outcome for the next day. </p>
        <div className="ag-theme-material" style={{ height: 380, width: 350}}>
          <AgGridReact
            rowData={rowData}
            columnDefs={columnDefs}
            animateRows={true}
          ></AgGridReact>
        </div>
        <button className="solarscore__prediction-button" onClick={requestData}>Predict</button>
      </div>
    </div>
  )
};

export default TestKatharina;



/* This is the example table with hard coded data
/* 
const [columnDefs] = useState ([
  {field: 'time'}, 
  {field: 'prediction'},
]);

const [rowData] = useState ([
  {time: "8:00", prediction: "890 W"}, 
  {time: "10:00", prediction: "1000 W"}, 
  {time: "12:00", prediction: "5000 W"}, 
  {time: "14:00", prediction: "5800 W"}, 
  {time: "16:00", prediction: "4800 W"},
  {time: "18:00", prediction: "3800 W"},
]);

return (
  <div className="solarscore__test section__margin" id="test">
    <div className="solarscore__test-heading">
      <h1 className="gradient-text">Test Katharina</h1>
      <h4> This is the private test region for Katharina and should not be removed. </h4>
      <button className="solarscore__test-button">Test Request</button>
      <div className="ag-theme-alpine" style={{height: 400, width: 400}}>
      <AgGridReact
          rowData={rowData}
          columnDefs={columnDefs}>
      </AgGridReact>
    </div>
    </div>
  </div>
)
} */





/* This is the 42 example code
/*   const [result, setLoadedData] = useState([]);

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
}; */
