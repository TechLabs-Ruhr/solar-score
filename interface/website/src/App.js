import React from 'react';
import { Navbar, TestPrediction, TestDenise, TestInka, TestKatharina, TestMarian, Footer, Header } from './components';
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


