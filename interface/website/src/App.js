import React from 'react';
import {Footer, Header, Signin} from './containers';
import {Navbar, Test, Test2} from './components';
import './App.css';

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
      <Test />
      <Test2 />
      <Footer />

  </div>
  )
}; 
export default App;

