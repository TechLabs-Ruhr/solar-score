import React, { useState, useEffect } from 'react';
import '../core/Prediction.css';
import axios from 'axios';
import { AgGridReact } from 'ag-grid-react';
import 'ag-grid-community/dist/styles/ag-grid.css';
import 'ag-grid-community/dist/styles/ag-theme-material.css';

const PowerTable = () => {
  const [rowData, setRowData] = useState([]);

  const [columnDefs] = useState([
    { field: 'time' },
    { field: 'prediction' },
  ]);

  const requestData = () => {
    axios
      .get('http://127.0.0.1:8000/powertable')
      .then((result) => {
        setRowData(result.data);
        console.log(result);
      })
      .catch((err) => {
        console.log(err);
      });
  };

  return (
    <div className="solarscore__prediction" id="test">
      <div className="solarscore__prediction-content">
        <h1 className="gradient-text">Prediction Table</h1>
        <p1> This table lists the predicted solar power outcome for the next ten days at your location. </p1>
        <div className="ag-theme-material" style={{ width: 1000, height: 300, }}>
          <AgGridReact
            rowData={rowData}
            columnDefs={columnDefs}
            animateRows={true}
          ></AgGridReact>
        </div>
        <button className="solarscore__prediction-button" onClick={requestData}>Predict</button>
        <p2> The process might take a few seconds. </p2>
      </div>
    </div>
  )
};

export default PowerTable;
