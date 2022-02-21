import React from 'react';
import { Signup } from '../../views/auth';
import {CTA, Navbar} from '../../components';
import './signuppage.css';


const SignupPage = () => {
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

export default SignupPage;
