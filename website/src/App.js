import React from 'react';
import {Footer, Possibility, Features, About, Header, Signin} from './containers';
import {CTA, Navbar} from './components';
import { Outlet, Link } from "react-router-dom";
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
      <About />
      <Features />
      <CTA />
      <Footer />
  </div>
  )
};

export default App;

