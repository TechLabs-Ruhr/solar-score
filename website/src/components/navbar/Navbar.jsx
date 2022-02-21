import React, {useState, useEffect, Fragment} from 'react';
import logo from '../../assets/logo.svg';
import './navbar.css';
import { Link } from 'react-router-dom';


const Navbar = () => {
  const [isAuth, setIsAuth] = useState(false);

  useEffect (() => {
    if (localStorage.getItem('token') !== null)
    {
      setIsAuth(true);
    }
  }, []);

  return (
    <div className="solarscore__navbar">
      <div className="solarscore__navbar-links-logo">
      <img src ={logo} alt = "logo" />
      </div>
      {isAuth === true ? (
          <Fragment>
            {' '}
            <div className="solarscore__navbar-sign">
              <Link to='/logout'>Logout</Link>
            </div>
            <div className="solarscore__navbar-sign">
              <Link to='/dashboard'>
              <button type="button"> Dashboard</button>
              </Link>
            </div>
          </Fragment>
        ) : (
          <Fragment>
            {' '}
            <div className="solarscore__navbar-sign">
              <p><Link to="/login">Login</Link></p>
            </div>
            <div className="solarscore__navbar-sign">
              <Link to ="/signup">
              <button type="button">Sign Up</button>
              </Link>
            </div>
          </Fragment>
        )}
        </div>
        
  ); 
};

export default Navbar;
