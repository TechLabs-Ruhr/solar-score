import React from 'react';
import { Navbar, TestPrediction, TestDenise, TestInka, TestKatharina, TestMarian, Footer, Header, TestKatharina_datatable } from './components';
import './App.css';

const App = () => {
  return (
    <div className="App">
      <Navbar />
      <Header />
      {/* <TestPrediction />
      <TestInka />
      <TestMarian />
      <TestDenise />
      <TestKatharina />
      <TestKatharina_datatable /> */}
      <Footer />
    </div>
  )
};
export default App;


