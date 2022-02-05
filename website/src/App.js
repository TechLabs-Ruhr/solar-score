import React from 'react';
import {Footer, Possibility, Features, About, Header} from './containers';
import {CTA, Brand, Navbar} from './components';
import './App.css';

const App = () => {
  return (
    <div className="App">
      <div className="gradient__bg">
        <Navbar />
        <Header />
      </div>
      <Brand />
      <About />
      <Features />
      <CTA />
      <Footer />
  </div>
  )
};

export default App;

