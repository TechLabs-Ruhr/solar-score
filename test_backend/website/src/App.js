import React from 'react';
import {Footer, Possibility, About, Header, Signin} from './containers';
import {Navbar} from './components';
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
      <Footer />
  </div>
  )
};

export default App;
