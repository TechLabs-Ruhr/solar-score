import React, { useState, useEffect } from 'react';
import './Prediction.css';
import { AgGridReact } from 'ag-grid-react';
import 'ag-grid-community/dist/styles/ag-grid.css';
import 'ag-grid-community/dist/styles/ag-theme-alpine.css';

const TestKatharina_datatable = () => {

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
    <div className="solarscore__prediction section__margin" id="test">
      <div className="solarscore__prediction-content">
        <h1 className="gradient-text">Test Katharina</h1>
        <h4> This is the private test region for Katharina and should not be removed. </h4>
        <div className="ag-theme-alpine" style={{height: 400, width: 400}}>
        <AgGridReact
            rowData={rowData}
            columnDefs={columnDefs}>
        </AgGridReact>
      </div>
      </div>
    </div>
  )
  }

export default TestKatharina_datatable;



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
