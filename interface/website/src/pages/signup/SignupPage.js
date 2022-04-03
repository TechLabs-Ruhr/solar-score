import React from 'react';
import  Signup from '../../views/auth/signup/Signup';
import {CTA, Navbar} from '../../components';
import './signuppage.css';


const SignupPage = () => {
  return (
    <div className="Signup">
     <Navbar />
      <div className="section__margin">
      <Signup/>
      </div>
  </div>
  )
};

export default SignupPage;
