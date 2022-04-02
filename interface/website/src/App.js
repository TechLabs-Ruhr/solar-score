import React from 'react';
import { Footer, Header, Signin } from './containers';
import { Navbar, TestPrediction, TestDenise, TestInka, TestKatharina, TestMarian } from './components';
import './App.css';

const App = () => {
  return (
    <div className="App">
      <Navbar />
      <Header />
      <TestPrediction />
      <TestInka />
      <TestMarian />
      <TestDenise />
      <TestKatharina />
      <Footer />
    </div>
  )
};
export default App;


