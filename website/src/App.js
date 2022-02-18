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
        <Routes>
          <Route path='/login' element={<Login/>} exact />
          <Route path='/signup' element={<Signup/>} exact />
          <Route path='/logout' element={<Logout/>} exact />
          <Route path='/dashboard' element={<Dashboard/>} exact />
        </Routes>
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

