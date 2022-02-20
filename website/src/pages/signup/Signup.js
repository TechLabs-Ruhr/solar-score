import React from 'react';
import {Signup} from '../../containers/index';
import {CTA, Navbar} from '../../components';
import './signup.css';


const Signup = () => {
  return (
    <div className="Signup">
     <div className="gradient__bg">
     <Navbar />
     </div>
      <div className="solarscore__flexheader gradient__bg section__margin">
      <Signup/>
      </div>
  </div>
  )
};

export default Signup;
