import React from 'react';
import { Signin } from '..';
import './header.css';

const Header = () => {
  return <div className="solarscore__header section__margin" id="home">
    <div className="solarscore__header-content">
      <h1 className="gradient__text"> Welcome To SolarScore</h1>
      <p>With precice predictions we help you to get most out of your solar plant. Get started and sign up your solar plant now.</p>
    </div>
  </div>
};

export default Header;