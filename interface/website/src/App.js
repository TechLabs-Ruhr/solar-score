import React from 'react';
import {Footer, Header, Signin} from './containers';
import {Navbar, TestInka, TestMarian} from './components';
import './App.css';
import TestArray from './components/test/ArrayPlotlyTest';

const App = () => {
  return (
    <div className="App">
     <div className="gradient__bg">
     <Navbar />
     </div>
      <div className="solarscore__flexheader gradient__bg section__margin">
      <Header />
      <Signin />
      </div>
      <TestInka />
      <TestMarian />
      <TestArray />
      <Footer />

  </div>
  )
}; 
export default App;


