import React from 'react';
import Login from '../../views/auth/login/Login';
import { Navbar} from '../../components';
import './loginpage.css';


const LoginPage = () => {
  return (
    <div className="Login">
     <Navbar />
      <div className="section__margin">
      <Login/>
      </div>
  </div>
  )
};

export default LoginPage;
