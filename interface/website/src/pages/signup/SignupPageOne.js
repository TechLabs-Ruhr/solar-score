import React from 'react';
import { Signup } from '../../views/auth';
import {CTA, Navbar} from '../../components';
import './signuppage.css';


const SignupPageOne = () => {
  return (
    <div className="Signup">
     <div className="gradient__bg">
     <Navbar />
     </div>
      <div className="solarscore__flexheader gradient__bg section__margin">
      <h1>Signup Step 1 </h1>
      </div>
  </div>
  )
};

export default SignupPageOne;
