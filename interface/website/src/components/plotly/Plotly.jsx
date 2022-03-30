import React from 'react';
import './plotly.css';
import Plot from "react-plotly.js"

function Plotly (props) {

    const linspaceFn = (startValue, stopValue, cardinality) => {
    var arr = [];
    var step = (stopValue - startValue) / (cardinality - 1);
    for (var i = 0; i < cardinality; i++) {
      arr.push(parseFloat((startValue + (step * i)).toFixed(3)));
    }
    return arr;
  }
    const t = linspaceFn(0, 20, 100)
    const x = t.map(i => (Math.cos(i)))
    const y = t.map(i => Math.sin(i))
    const z = t


  return (
    <div className="solarscore__test section__margin"  id="test">
      <div className="solarscore__test-heading">
        <h1 className="gradient-text">Plotly Test </h1>
        <Plot
          onClick={(data) => {
            console.log(data.points[0])
          }}
        data={[
          {
            x: x,
            y: y,
            z: z,
            mode: 'markers', 
            type:'scatter3d',
            marker: {
              size:12,
              color:z,     
              colorscale:'Viridis', 
              opacity:0.8
            }
          }
        ]}
        />
      </div>
      </div>
      ) 
  };

export default Plotly;


{/* <button className="solarscore__test-button" >Plotly Test</button> */}