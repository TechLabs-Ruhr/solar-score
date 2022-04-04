import React from 'react';
import './header.css';
import logo from '../../assets/logo_header.svg';
import { Link } from 'react-router-dom';

const Header = () => {
  return <div className="solarscore__header section__margin" id="home">
    <div className="solarscore__header-content">
      <h1 className="gradient__text"> Welcome To SolarScore</h1>
      <p>With precise predictions we help you to get most out of your solar plant.</p>
      <p>Get started and sign up your solar plant now.</p>
      <div className="solarscore__signup_button">
              <Link to ="/signup">
              <button type="button">Sign Up Here</button>
              </Link>
       </div>
    </div>
    <div className="solarscore__image solarscore__image_background">
        <img src = {logo} alt = "logo" />
      </div>
  </div>
};

export default Header;