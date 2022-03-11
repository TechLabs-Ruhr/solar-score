import React from 'react';
import { Login } from '../../views/auth';
import { Navbar} from '../../components';
import './loginpage.css';


const LoginPage = () => {
  return (
    <div className="Login">
     <div className="gradient__bg">
     <Navbar />
     </div>
      <div className="solarscore__flexheader gradient__bg section__margin">
      <Login/>
      </div>
  </div>
  )
};

export default LoginPage;
