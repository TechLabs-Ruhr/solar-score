import React from 'react';
import { Feature } from '../../components';
import './about.css';

const About = () => {
  return (
  <div className="solarscore__about section__margin"  id="about">
    <div className="solarscore__about-feature">
      <Feature/>
    </div>
    <div className="solarscore__about-heading">
    <h1 className="gradient-text">Heading </h1>
    <p> Paragraph</p>
    </div>
    </div>
    ) 
};

export default About;
