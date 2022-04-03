import React from 'react';
import  Logout from '../../views/auth/logout/Logout';
import {Footer, Navbar} from '../../components';
import './logoutpage.css';


const LogoutPage = () => {
  return (
    <div className="Logout">
     <Navbar />
      <div className="section__margin">
      <Logout/>
      </div>
      <Footer />
  </div>
  )
};

export default LogoutPage;
