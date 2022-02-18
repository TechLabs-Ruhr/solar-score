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
    <nav>
    <div className="solarscore__navbar">
    <div className="solarscore__navbar-links">
      <div className="solarscore__navbar-links-logo">
      <img src ={logo} alt = "logo" />
      </div>
      {isAuth === true ? (
          <Fragment>
            {' '}
            <div className="solarscore__navbar-sign">
              <Link to='../views/auth/logout'>Logout</Link>
            </div>
            <div className="solarscore__navbar-sign">
              <Link to='../views/dashboard'>
              <button type="button"> Dashboard</button>
              </Link>
            </div>
          </Fragment>
        ) : (
          <Fragment>
            {' '}
            <div className="solarscore__navbar-sign">
              <p><Link to='../views/auth/login'>Login</Link></p>
            </div>
            <div className="solarscore__navbar-sign">
              <Link to='../views/auth/signup'>
              <button type="button">Sign Up</button>
              </Link>
            </div>
          </Fragment>
        )}
        </div>
        </div>
       </nav>
  ); 
};

export default Navbar;
