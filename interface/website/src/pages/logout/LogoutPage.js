import React from 'react';
import  Logout from '../../views/auth/logout/Logout';
import {CTA, Navbar} from '../../components';
import './logoutpage.css';


const LogoutPage = () => {
  return (
    <div className="Logout">
     <div className="gradient__bg">
     <Navbar />
     </div>
      <div className="solarscore__flexheader gradient__bg section__margin">
      <Logout/>
      </div>
  </div>
  )
};

export default LogoutPage;
