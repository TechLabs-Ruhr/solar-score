import React from 'react';
import './footer.css';
import techlabs_logo from '../../assets/logo_techlabs.jpeg';

const Footer = () => {
  return (
    <div className = "solarscore__footer">
      <div className = "solarscore__footer-creator">
    <p>Created by:</p>
    <p>Denise</p>
    <p>Inka</p>
    <p>Katharina</p>
    <p>Marian</p>
    <p>Niklas</p>
    </div>
    <div className = "solarscore__footer-supporter">
    <p>Supported by:</p>
    <p >TechLabs Dortmund</p>
    <div className="techlabs_logo">
        <img src = {techlabs_logo} alt = "techlabs logo" width="30" height="30" />
      </div>
    </div>
  </div>
  )
  
};

export default Footer;