import React from 'react';
import {Footer, Possibility, Features, About, Header, Signin, Signup, Login, Logout, Dashboard} from './containers';
import {CTA, Navbar} from './components';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css';


const App = () => {
  return (
    <div className="App">
   <Router>
     <div className="gradient__bg">
     <Navbar />
     </div>
      </Router>
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

